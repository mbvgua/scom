from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)

from app.database import engine, Base, User, Blog


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    elegently handle startup/shutdown events.
    this is an idempotent action that creates the database models imported.
    also has automatic cleanup
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app: FastAPI = FastAPI(
    title="scom",
    description="main scom website",
    version="0.0.1",
    lifespan=lifespan,
    # enable this once the project goes live, to disable the api docs
    # openapi_url=None,
)

# ensure paths are absolute for vercel
BASE_DIR = Path(__file__).resolve().parent.parent

# define styling and templates to use
templates: Jinja2Templates = Jinja2Templates(directory=BASE_DIR / "templates")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# import and register the routes
from app.routes import router as app_router
from app.api import router as api_router

app.include_router(app_router)
app.include_router(api_router)


# error handling
@app.exception_handler(StarletteHTTPException)
async def general_http_exception_handler(
    request: Request, exception: StarletteHTTPException
):
    """
    handle exception errors asynchronously.
    this catches any StarletteHTTPException's raised via code execution.

    fastapi is built on top of starlette, hence why its execptions are also imported
    alongside those of fastapi, lest some will be missed.
    """
    # if url starts with "/api/..."
    if request.url.path.startswith("/api"):
        return await http_exception_handler(request, exception)

    message = (
        exception.detail
        if exception.detail
        else "An error occurred. Please check your request and try again?"
    )

    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "title": f"Error {exception.status_code}",
            "error_code": exception.status_code,
            "error_message": message,
        },
        status_code=exception.status_code,
    )


# Catch ANY unhandled exception (500 Internal Server Error)
@app.exception_handler(Exception)
async def custom_500_handler(request: Request, exception: Exception):
    """
    handle all the other server crashes not handled above.this is aimed at 5xx
    server codes, that mean an issue with the internal server. will most
    definetly not be present in a prod ennvironement(after deploying), but you
    never know ;)
    """
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "title": "Error 500",
            "error_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "error_message": "Internal Server",
        },
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


# Validation Error Handling
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exception: RequestValidationError
):
    """
    handle validation errors asynchronously
    mostly via forms, or invalid data types while making requests
    """

    # if url starts with "/api/..." return JSON response
    if request.url.path.startswith("/api"):
        return await request_validation_exception_handler(request, exception)

    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "title": f"Error {status.HTTP_422_UNPROCESSABLE_CONTENT}",
            "error_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "error_message": f"Error: {exception.errors()}",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )
