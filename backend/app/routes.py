from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database import get_db
from backend.app import schemas, models, utils

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.UserModel).where(models.UserModel.email == user_data.email))
    user = result.scalars().first()

    if user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="error: user already exists.")

    new_user = models.UserModel(email=user_data.email, password=utils.hash_password(user_data.password))

    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

@router.post("/login", response_model=schemas.UserResponse, status_code=status.HTTP_202_ACCEPTED)
async def login(user_data: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.UserModel).where(models.UserModel.email == user_data.email))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="error: user not found.")

    if not utils.verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="error: incorrect password.")

    token = utils.create_access_token(data={"sub": user.email})
    return {"access token": token, "token_type": "bearer"}




    

    
    


        



    





