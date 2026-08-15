"""
utility functions for working with the blogs section.
it contains 2 functions:
    - get_all_blogs
    - get_blog_by_id
"""

import os
from datetime import datetime

import frontmatter

CONTENT_DIR = "content"


def get_all_blogs():
    """
    helper function reads all ".md" files from the CONTENT_DIR, and parses them
    to be displayed on the app pages

    this is much easier than adding db I guess?
    """
    blogs = []

    # if path doesn't exist return false
    if not os.path.exists(CONTENT_DIR):
        return blogs

    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(CONTENT_DIR, filename)

            with open(filepath, "r") as f:
                post = frontmatter.load(f)

                # Map frontmatter to template-friendly dictionary
                blog_data = {
                    "id": post.get("id"),
                    "title": post.get("title", "Untitled"),
                    "slug": post.get("slug", ""),
                    "author": post.get("author", "Unknown"),
                    # yeah its hard-coded. whoops!
                    "avatar": f"/static/images/profile_pics/{post.get("author")}.png",
                    "image": f"{post.get("cover")}",
                    "date_posted": datetime.now(),  # cant touch this. wowowowo..
                    "last_modified": post.get("last_modified", datetime.now()),
                    "tags": post.get("tags"),
                    "draft": post.get("draft"),
                    "content": post.content,
                }
                blogs.append(blog_data)

    # keep posts where draft is not True / "true"
    published_blogs = [
        blog
        for blog in blogs
        if not blog.get("draft") or str(blog.get("draft")).lower() == "false"
    ]

    # return sorted list in descending order, newest first
    published_blogs.sort(key=lambda x: x["date_posted"], reverse=True)
    return published_blogs


def get_blog_by_slug(slug: str):
    """
    function that gets a specific blog by its slug
    """
    blogs = get_all_blogs()

    for blog in blogs:
        # Check if blog has an 'slug' and compare as lowercase strings
        if blog.get("slug") and blog["slug"].strip().lower() == slug.strip().lower():
            return blog

    return None
