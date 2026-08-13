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
                    "avatar": f"/static/images/{post.get("author")}.png",
                    "image": f"/static/images/blogs/{post.get("image")}",
                    "date_posted": post.get("date_posted"),
                    "date_modified": post.get("date_modified", datetime.now()),
                    "tags": post.get("tags"),
                    "content": post.content,
                }
                blogs.append(blog_data)

    # sort blogs in descending order, newest first
    blogs.sort(key=lambda x: x["date_posted"], reverse=True)
    return blogs


def get_blog_by_id(blog_id: int):
    """
    function that gets a specific blog by its id
    """
    blogs = get_all_blogs()

    for blog in blogs:
        if str(blog["id"] == str(blog_id)):
            return blog

    return None
