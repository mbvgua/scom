from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.main import templates
from app.schemas.posts import PostCategory
from app.utils.blogs import get_all_blogs, get_blog_by_id

router = APIRouter(tags=["views"])


@router.get("/")
async def home(request: Request):
    """
    renders the "home.html" template on the "/" URL
    landing page where users view the application
    """

    title: str = "Homepage"

    # get latest 3 blogs from the db
    blogs = get_all_blogs()

    return templates.TemplateResponse(
        request, "home.html", {"title": title, "blogs": blogs[:3]}, status.HTTP_200_OK
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


@router.get("/blog-list")
async def blog_list(
    request: Request,
    category: Optional[PostCategory] = None,
):
    """
    renders the "blog_list.html" on the "/blog-list" URL.
    it takes in an optional, "category" filter, that shows blogs matching the
    selected category
    """
    title: str = "Blog List"

    blogs = get_all_blogs()
    if category:
        blogs = [b for b in blogs if category.lower() in b.get("tags", "").lower()]

        return templates.TemplateResponse(
            request,
            "blog_list.html",
            {"title": title, "blogs": blogs, "current_category": category},
            status.HTTP_200_OK,
        )

    return templates.TemplateResponse(
        request, "blog_list.html", {"title": title, "blogs": blogs}, status.HTTP_200_OK
    )


@router.get("/blog-post/{blog_id}")
async def blog_post(request: Request, blog_id: int):
    """
    renders the "blog_post.html" on the "/blog-post" URL.

    TODO:
    - incomplete route, add the "slug" section for urls
    """
    title: str = "Blog Post"

    blog = get_blog_by_id(blog_id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Oh no! Blog post not found... try again?",
        )

    return templates.TemplateResponse(
        request, "blog_post.html", {"title": title, "blog": blog}, status.HTTP_200_OK
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
