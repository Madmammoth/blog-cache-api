class PostService:
    @staticmethod
    async def get_post(post_id: int):
        from app.repositories.post_repository import PostRepository

        post = await PostRepository.get(post_id)

        if not post:
            return None

        return post
