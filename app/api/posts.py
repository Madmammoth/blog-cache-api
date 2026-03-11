from fastapi import APIRouter, HTTPException, status

from app.schemas.post import PostResponse, PostCreate
from app.services.post_service import PostService

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)


@router.post(
    "",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_post(data: PostCreate):
    post = await PostService.create_post(data)
    return post


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    post = await PostService.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/{post_id}", response_model=PostResponse)
async def update_post(post_id: int, data: PostCreate):
    post = await PostService.update_post(post_id, data)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.delete(
    "/{post_id}",
    response_model=PostResponse,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_post(post_id: int):
    deleted = await PostService.delete_post(post_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")

    return {"status": "deleted"}
