from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import Blog, get_db
from app.main import templates
from app.schemas import PostCategory

router = APIRouter(tags=["views"])


@router.get("/")
async def home(request: Request, db: Annotated[AsyncSession, Depends(get_db)]):
    """
    the main application endpoint
    renders the "home.html" template on the "/" URL
    asynchronous so that it can interact with the database using dependency
    injection

    NOTE:
    - "order_by()": arranges them in descending order such that newest posts
      come first.
    """

    title: str = "Homepage"

    # get blogs from the db. 3 only
    data = await db.execute(select(Blog).order_by(Blog.last_updated.desc()))
    blog = data.scalars().all()

    return templates.TemplateResponse(
        request, "home.html", {"title": title, "blogs": blog[:3]}, status.HTTP_200_OK
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
    db: Annotated[AsyncSession, Depends(get_db)],
    category: Optional[PostCategory] = None,
):
    """
    renders the "blog_list.html" on the "/blog-list" URL.
    it takes in an optional, "category" filter, that shows blogs matching the
    selected category
    this data is fetched asynchronously from the database, using dependency injection
    """
    title: str = "Blog List"

    data = await db.execute(select(Blog))
    blogs = data.scalars().all()

    if category:
        data = await db.execute(select(Blog).where(Blog.tags == category))
        blogs = data.scalars().all()

        return templates.TemplateResponse(
            request,
            "blog_list.html",
            {"title": title, "blogs": blogs, "current_category": category},
            status.HTTP_200_OK,
        )

    return templates.TemplateResponse(
        request, "blog_list.html", {"title": title, "blogs": blogs}, status.HTTP_200_OK
    )


# incomplete route, add the "slug" URL
@router.get("/blog-post/{blog_id}")
async def blog_post(
    request: Request, db: Annotated[AsyncSession, Depends(get_db)], blog_id: int
):
    """
    renders the "blog_post.html" on the "/blog-post" URL.
    this data is fetched asynchronously from the database, using dependency injection

    NOTE:
    - "selectinload()": allows for eargely loading in the async sqlite session,
      hence the request is able to access therelated table "Blog.author", lest
      it would return a "missing greenlet error": https://sqlalche.me/e/20/xd2s
    """
    title: str = "Blog Post"

    data = await db.execute(
        select(Blog).options(selectinload(Blog.author)).where(Blog.id == blog_id)
    )
    blog = data.scalars().first()

    return templates.TemplateResponse(
        request,
        "blog_post.html",
        {"title": title, "blog": blog, "author": blog.author.name},
        status.HTTP_200_OK,
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
