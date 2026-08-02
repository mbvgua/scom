import datetime

from sqladmin import Admin, ModelView
from sqlalchemy.orm import selectinload

from app.database import Blog, User


class UserAdmin(ModelView, model=User):
    """
    define the "Users" admin page

    NOTE:
    - column_list: columns to show in the main list view
    - column_searchable_list: column values you can search with
    - column_sortable_list: columns you can sort with, in ascending or
      descending order
    - column_filterable_list: columns to filter with
    - form_columns: fields to show when creating/updating a users values

    TODO:
    - add email validation
    - create password hashing function during create/update
    - ensure "role" is validated against itstype during update/editing
    """

    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"

    column_list = [User.id, User.name, User.role, User.email]
    column_searchable_list = [User.id, User.role, User.name]
    column_sortable_list = [User.id]
    column_filterable_list = [User.role]

    # form fields to allow during creation/editing
    form_columns = [User.name, User.email, User.password_hash, User.role, User.avatar]


class BlogAdmin(ModelView, model=Blog):
    """
    define the "Blogs" admin page

    NOTE:
    - column_list: columns to show in the main list view
    - column_searchable_list: column values you can search with
    - column_sortable_list: columns you can sort with, in ascending or
      descending order
    - column_filterable_list: columns to filter with

    TODO:
    - when creating new blogs, allows creation using markdown
    - blog.author still show a memory address in detailed view, make it show
      the author.name instead
    - details_template: allows me to add a custom, templatefor the blog
      editing/updating, where I can now embedd a simple js based markdown
      editotr into it allowingfor much easier content addition/modification
    """

    @staticmethod
    def format_datetime(value: datetime.datetime) -> str:
        """
        format the date, to be human readable. this allows formatting in both the
        list view and the detail view
        """
        return value.strftime("%b %d, %Y - %H:%M UTC") if value else "N/A"

    name = "Blog"
    name_plural = "Blogs"
    icon = "fa-solid fa-file-text"

    details_template = "sqladmin/layout.html"

    column_list = [Blog.id, Blog.title, Blog.author, Blog.user_id, Blog.last_updated]
    column_searchable_list = [Blog.tags, Blog.title, Blog.author]
    column_sortable_list = [Blog.id, Blog.user_id]
    column_filterable_list = [Blog.tags]

    # apply datetime formatting globally to list and detail views
    column_type_formatters = {datetime.datetime: format_datetime}

    # Explicitly format how the 'author' column renders in the main table
    column_formatters = {
        Blog.author: lambda model, a: (
            model.author.name[:100] + "..." if model.author else "No Author"
        ),
    }
