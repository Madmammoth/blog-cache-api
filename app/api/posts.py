from fastapi import APIRouter, HTTPException

from app.schemas.post import PostResponse
from app.services.post_service import PostService

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    post = await PostService.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
