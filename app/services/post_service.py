import json

from app.cache.redis_client import redis_client
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

    @staticmethod
    async def update_post(post_id: int, data):
        post = await PostRepository.update(
            post_id=post_id,
            title=data.title,
            content=data.content,
        )

        if not post:
            return None

        cache_key = f"post: {post_id}"
        await redis_client.delete(cache_key)

        return post
