from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app: FastAPI = FastAPI(
    title="scom",
    description="main scom website",
    version="0.0.1",
)

# define styling and templates to use
templates: Jinja2Templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# import and register the routes
from app.routes import router

app.include_router(router)
