from typing import List

from datetime import UTC, datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.config import Base
from app.schemas.users import UserRoles


class User(Base):
    """
    define the "users" table, inheriting from the "Base" class defined above
    the table contains the following columns:
        - id
        - name
        - email
        - password_hash
        - role
        - avatar
        - blogs

    NOTE:
    - "Mapped": allows for type hints in our app
    - "relationship": forward-references the "Blog" table. afterwhich
      "back_populates" links to the "author" column in Blogs, allowing one to
      perform actions like
      User.blogs.[id,title,last_updated,images,tags,content]
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(300), nullable=False)
    role: Mapped[UserRoles] = mapped_column(String(50), nullable=False)
    avatar: Mapped[str] = mapped_column(String(200), nullable=True)
    blogs: Mapped[list["Blog"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )

    def __str_(self) -> str:
        return f"{self.name} ({self.email})"


class Blog(Base):
    """
    define the "blogs" table, inheriting from the "Base" class defined above.
    the table contains the following columns:
        - id
        - user_id
        - title
        - last_updated
        - images []
        - tags []
        - content

    NOTE:
    - "Mapped": allows for type hints in our app
    - "relationship": references the "User" table. afterwhich
      "back_populates" links to the "blogs" column in User, allowing one to
      perform actions like
      Blog.author.[id,name,email,password_hash,role,avatar]
    """

    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), index=True, nullable=False
    )
    title: Mapped[str] = mapped_column(String(500), unique=True, nullable=False)
    last_updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC), nullable=False
    )
    # images: how toupload a list of images
    tags: Mapped[List[str]] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped["User"] = relationship(back_populates="blogs")

    def __str__(self) -> str:
        return self.title
