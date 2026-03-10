from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.posts import router as posts_router
from app.db.session import engine
from app.models.post import Base


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(posts_router)
