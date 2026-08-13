"""
creates config for our asynchronous database connection. being async its able
to perform non-blocking operations

the seconf part also defines our database models, which are currently 2:
    - User
    - Blog
"""

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

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
