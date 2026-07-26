from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
