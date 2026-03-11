import pytest_asyncio

from app.cache.redis_client import redis_client


@pytest_asyncio.fixture(autouse=True)
async def clear_cache():
    await redis_client.flushdb()
    yield
    await redis_client.flushdb()
