from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from model import Post,Comment
from auth import get_current_user
from database import get_session

router = APIRouter(prefix="/comments")

@router.post("/{post_id}")
def add_comment(
    post_id: int,
    text: str,
    user=Depends(get_current_user),
    session=Depends(get_session)
):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(404, "Post not found")

    comment = Comment(
        text=text,
        user_id=user.id,
        post_id=post_id
    )

    session.add(comment)
    session.commit()

    return comment


@router.get("/{post_id}")
def get_comments(post_id: int, session=Depends(get_session)):
    comments = session.exec(
        select(Comment).where(Comment.post_id == post_id)
    ).all()

    return comments