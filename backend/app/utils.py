from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
from backend.settings import settings

from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def hash_password(password: str) -> str:
    return pwd_context.hash(password)

async def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

async def create_access_token(data: dict, expires_data: timedelta = timedelta(hours=1)) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_data
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)) -> str :
    credentials_execepition = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="error: could not validate credentials.",
        headers={"www-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_execepition
        return email
        
    except JWTError:
        raise credentials_execepition
