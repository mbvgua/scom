"""
creates config for our asynchronous database connection. being async its able
to perform non-blocking operations

the seconf part also defines our database models, which are currently 2:
    - User
    - Blog
"""

from typing import List

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.schemas import UserRoles
from app.config import settings

# for translating Python SQL statements into raw SQL for sqlite
engine = create_async_engine(
    settings.sqlalchemy_database_url,
    # sqlite is synchronous by nature, fastapi disables this, allowing for
    # non-blocking operations
    connect_args={"check_same_thread": False},
)
# generate async dab session whenever you need to perform an operation
async_session_local = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    """
    inherited by every database table/model in your application (e.g., User, Post)
    It registers your models with SQLAlchemy's metadata so tables can be created
    automatically using Base.metadata.create_all(bind=engine)
    """

    pass


async def get_db():
    """
    create a new database session for the duration of an incomming HTTPRequest.
    it will be referenced by all our routes, that perform database operations
    via DI(dependecy injection).
    cleanup happens automatically and possible rollbacks if error occurs
    """
    async with async_session_local() as db:
        yield db


from datetime import UTC, datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


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
    blogs: Mapped[list[Blog]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )


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
    author: Mapped[User] = relationship(back_populates="blogs")
