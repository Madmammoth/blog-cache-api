import json

from app.cache.redis_config import redis_client
from app.repositories.post_repository import PostRepository
from app.schemas.post import PostCreate


class PostService:
    @staticmethod
    async def get_post(post_id: int):
        cache_key = f"post:{post_id}"
        cached = await redis_client.get(cache_key)

        if cached:
            return json.loads(cached)

        post = await PostRepository.get(post_id)

        if not post:
            return None

        post_data = {
            "id": post.id,
            "title": post.title,
            "content": post.content,
        }

        await redis_client.set(cache_key, json.dumps(post_data), ex=3600)

        return post_data

    @staticmethod
    async def create_post(data: PostCreate):
        post = await PostRepository.create(
            title=data.title,
            content=data.content,
        )

        return post
