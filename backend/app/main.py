from routes import router as auth_router
from fastapi import FastAPI
from app.database import Base

app = FastAPI()

app.include_router(auth_router.router)

async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)