from fastapi import APIRouter

from app.schemas.post import PostResponse

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    return {"message": "not implemented"}
