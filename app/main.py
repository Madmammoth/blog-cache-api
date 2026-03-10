from fastapi import FastAPI
from app.api.posts import router as posts_router

app = FastAPI()

app.include_router(posts_router)
