import pytest
from httpx import ASGITransport, AsyncClient

from app.cache.redis_client import redis_client
from app.main import app


@pytest.mark.asyncio
async def test_post_cache():
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post(
            "/posts",
            json={
                "title": "Test title",
                "content": "Test content",
            },
        )

        assert response.status_code == 200

        post = response.json()

        assert post["title"] == "Test title"
        assert post["content"] == "Test content"

        post_id = post["id"]
        cache_key = f"post:{post_id}"

        assert await redis_client.get(cache_key) is None

        await client.get(f"/posts/{post_id}")
        cached = await redis_client.get(cache_key)

        assert cached is not None
