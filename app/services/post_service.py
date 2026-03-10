from app.repositories.post_repository import PostRepository
from app.schemas.post import PostCreate


class PostService:
    @staticmethod
    async def get_post(post_id: int):
        post = await PostRepository.get(post_id)

        if not post:
            return None

        return post

    @staticmethod
    async def create_post(data: PostCreate):
        post = await PostRepository.create(
            title=data.title,
            content=data.content,
        )

        return post
