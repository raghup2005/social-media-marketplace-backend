




from fastapi import APIRouter, Depends
from model import Post
from auth import get_current_user
from database import get_session

router = APIRouter(prefix="/posts")

@router.post("/")
def create_post(content: str, user=Depends(get_current_user), session=Depends(get_session)):
    post = Post(content=content, user_id=user.id)
    session.add(post)
    session.commit()
    return post