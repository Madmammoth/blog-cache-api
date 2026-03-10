from sqlalchemy import select

from app.db.session import session_maker
from app.models.post import Post


class PostRepository:
    @staticmethod
    async def get(post_id: int):
        async with session_maker() as session:
            stmt = select(Post).where(Post.id == post_id)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()

    @staticmethod
    async def create(title: str, content: str):
        async with session_maker() as session:
            post = Post(title=title, content=content)
            session.add(post)
            await session.commit()
            await session.refresh(post)
            return post
