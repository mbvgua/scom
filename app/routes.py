from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse

from app.main import templates

router = APIRouter(tags=["views"])


@router.get("/")
def home(request: Request, response_class=HTMLResponse):
    """
    "/" the main application endpoint
    """

    title: str = "Homepage"
    return templates.TemplateResponse(
        request, "home.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/about-us")
def about_us(request: Request, response_class=HTMLResponse):
    """
    "/about-us" page
    """
    title: str = "About Us"
    return templates.TemplateResponse(
        request, "about-us.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/programs")
def programs(request: Request):
    """
    "/programs" page
    """
    title: str = "Programs"
    return templates.TemplateResponse(
        request, "programs.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/get-involved")
def get_involved(request: Request):
    """
    "/get-involved" page
    """
    title: str = "Get Involved"
    return templates.TemplateResponse(
        request, "get-involved.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/contact-us")
def contact_us(request: Request):
    """
    "/contact-us" page
    """
    title: str = "Contact Us"
    return templates.TemplateResponse(
        request, "contact-us.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/donate")
def donate(request: Request):
    """
    "/donate" page
    """
    title: str = "Donate"
    return templates.TemplateResponse(
        request, "donate.html", {"title": title}, status.HTTP_200_OK
    )
