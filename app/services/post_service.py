import json

from app.cache.redis_client import redis_client
from app.repositories.post_repository import PostRepository
from app.schemas.post import PostCreate, PostResponse


class PostService:
    @staticmethod
    async def get_post(post_id: int) -> PostResponse | None:
        cache_key = f"post:{post_id}"
        cached = await redis_client.get(cache_key)

        if cached:
            data = json.loads(cached)
            return PostResponse(**data)

        post = await PostRepository.get(post_id)

        if not post:
            return None

        post_response = PostResponse.model_validate(post)

        await redis_client.set(
            cache_key, json.dumps(post_response.model_dump()), ex=3600
        )

        return post_response

    @staticmethod
    async def create_post(data: PostCreate) -> PostResponse:
        post = await PostRepository.create(
            title=data.title,
            content=data.content,
        )

        return PostResponse.model_validate(post)

    @staticmethod
    async def update_post(post_id: int, data) -> PostResponse | None:
        post = await PostRepository.update(
            post_id=post_id,
            title=data.title,
            content=data.content,
        )

        if not post:
            return None

        cache_key = f"post:{post_id}"
        await redis_client.delete(cache_key)

        return PostResponse.model_validate(post)

    @staticmethod
    async def delete_post(post_id: int) -> bool:
        deleted = await PostRepository.delete(post_id)

        if not deleted:
            return False

        cache_key = f"post:{post_id}"
        await redis_client.delete(cache_key)

        return True
