from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
import schemas, models, utils

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: schemas.BaseModel, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.UserModel).where(models.UserModel.email == user_data.email))
    user = resutt.scalars().first()

    if user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="error: user already exists.")

    new_user = models.UserModel(email=user_data.email, password=utils.hash_password(user_data.password))
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user



    





