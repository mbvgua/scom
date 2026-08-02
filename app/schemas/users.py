"""
defines the schemas for "Users " within the app.
this helps inimproved data validation and also editor type hinting using
pydantic models, now I no longer guess my types!(User.*)

defines the following schemas:
    - UserRoles
"""

from enum import Enum


class UserRoles(str, Enum):
    """
    defines user roles in the app, which in turn dictates the users permission
    authorization
    """

    admin = "admin"
    editor = "editor"
