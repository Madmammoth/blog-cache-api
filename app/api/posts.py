from fastapi import APIRouter

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)


@router.get("/{post_id}")
async def get_post(post_id: int):
    return {"message": "not implemented"}
