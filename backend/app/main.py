from backend.app.routes import router 
from fastapi import FastAPI
from backend.app.database import Base, engine

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)