from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from sqlmodel import select
from fastapi import Depends,HTTPException
from database import*
from model import *


SECRET_KEY = "secret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["argon2"])

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=30)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str, session=Depends(get_session)):
    payload = jwt.decode(token, "secret", algorithms=["HS256"])
    user = session.exec(select(User).where(User.email == payload.get("sub"))).first()
    if not user:
        raise HTTPException(401, "invalid")
    return user