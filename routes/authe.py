from fastapi import FastAPI,Depends,HTTPException,APIRouter
from sqlmodel import SQLModel,select
from auth import *
from database import *






router = APIRouter(prefix="/auth")

@router.post("/register")
def register(name: str, email: str, password: str, session=Depends(get_session)):
    user = User(name=name, email=email, hashed_password=hash_password(password))
    session.add(user)
    session.commit()
    return {"msg": "registered"}

@router.post("/login")
def login(email: str, password: str, session=Depends(get_session)):
    user = session.exec(select(User).where(User.email == email)).first()
    if not user or not verify_password(password, user.hashed_password):
        return {"error": "invalid"}
    token = create_token({"sub": user.email})
    return {"access_token": token}