from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from routes import authe, posts, products,comments,likes

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(authe.router)
app.include_router(posts.router)
app.include_router(products.router)

app.include_router(likes.router)
app.include_router(comments.router)