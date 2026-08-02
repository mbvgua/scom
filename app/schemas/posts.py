"""
defines the schemas for "Posts " within the app.
this helps inimproved data validation and also editor type hinting using
pydantic models, now I no longer guess my types

defines the following schemas:
    - PostCategory
"""

from enum import Enum


class PostCategory(str, Enum):
    """
    defines the categories of posts to beused in the application
    must coincide with the categories defined in the "templates/blog_list.html"
    file(mini-header section), lest some of the categories will not be seen
    """

    stories = "stories"
    updates = "updates"
    events = "events"
    impact = "impact"
