from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from model import Post,Like
from auth import get_current_user
from database import get_session

router = APIRouter(prefix="/likes")

@router.post("/{post_id}")
def like_post(
    post_id: int,
    user=Depends(get_current_user),
    session=Depends(get_session)
):
    # check post exists
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(404, "Post not found")

    # prevent duplicate likes
    existing = session.exec(
        select(Like).where(
            Like.user_id == user.id,
            Like.post_id == post_id
        )
    ).first()

    if existing:
        raise HTTPException(400, "Already liked")

    like = Like(user_id=user.id, post_id=post_id)
    session.add(like)
    session.commit()

    return {"message": "Post liked"}