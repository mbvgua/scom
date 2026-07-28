from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)

from pathlib import Path

app: FastAPI = FastAPI(
    title="scom",
    description="main scom website",
    version="0.0.1",
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


# Validation Error Handling
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exception: RequestValidationError
):
    """
    handle validation errors asynchronously
    """

    # if url starts with "/api/..." return JSON response
    if request.url.path.startswith("/api"):
        return await request_validation_exception_handler(request, exception)

    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "title": f"Error {exception.status_code}",
            "error_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "error_message": "Invalid request, please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )
