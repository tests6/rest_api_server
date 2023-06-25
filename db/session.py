from sqlalchemy.ext.asyncio import create_async_engine

from sqlmodel.ext.asyncio.session import AsyncSession

from settings import Settings

settings = Settings()
db_url = f"{settings.db_protocol}://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
engine = create_async_engine(db_url, future=True)


async def get_session():
    async with AsyncSession(engine) as session:
        yield session
