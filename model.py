from sqlmodel import SQLModel,Field
from pydantic import BaseModel
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True)
    hashed_password: str
    
    
    
class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    user_id: int 



class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    user_id: int

class Like(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    post_id: int
class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    user_id: int
    post_id: int