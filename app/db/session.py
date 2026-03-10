from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import Settings

settings = Settings()

engine = create_async_engine(
    settings.db_url.get_secret_value(),
    echo=True,
)

session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
)
