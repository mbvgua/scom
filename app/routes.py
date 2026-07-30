from fastapi import APIRouter, Request, status

from app.main import templates
from app.schemas import PostCategory

router = APIRouter(tags=["views"])


@router.get("/")
def home(request: Request):
    """
    the main application endpoint
    renders the "home.html" template on the "/" URL
    """

    title: str = "Homepage"
    return templates.TemplateResponse(
        request, "home.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/about-us")
def about_us(request: Request):
    """
    renders the "abouts_us.html" template on the "/about-us" URL
    """
    title: str = "About Us"
    return templates.TemplateResponse(
        request, "about_us.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/programs")
def programs(request: Request):
    """
    renders the "programs.html" template on the "/programs" URL
    """
    title: str = "Programs"
    return templates.TemplateResponse(
        request, "programs.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/get-involved")
def get_involved(request: Request):
    """
    renders the "get_involved.html" on the "/get-involved" URL
    """
    title: str = "Get Involved"
    return templates.TemplateResponse(
        request, "get_involved.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/contact-us")
def contact_us(request: Request):
    """
    renders the "contact_us.html" on the "/contact-us" URL
    """
    title: str = "Contact Us"
    return templates.TemplateResponse(
        request, "contact_us.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/donate")
def donate(request: Request):
    """
    renders the "donate.html" on the "/donate" URL
    """
    title: str = "Donate"
    return templates.TemplateResponse(
        request, "donate.html", {"title": title}, status.HTTP_200_OK
    )


# incomplete route, add the "slug" URL, and categories filter
@router.get("/blog-list")
def blog_list(request: Request):
    """
    "/blog-list" page
    """
    title: str = "Blog List"

    return templates.TemplateResponse(
            request, "blog_list.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/blog-post")
def blog_post(request: Request):
    """
    "/blog-post" page
    """
    title: str = "Blog Post"
    return templates.TemplateResponse(
        request, "blog_post.html", {"title": title}, status.HTTP_200_OK
    )


@router.get("/privacy-policy")
def privacy_policy(request: Request):
    """
    renders the "privacy_policy.html" on the "/privacy-policy" URL
    """
    title: str = "Privacy Policy"
    return templates.TemplateResponse(
        request, "privacy_policy.html", {"title": title}, status.HTTP_200_OK
    )
