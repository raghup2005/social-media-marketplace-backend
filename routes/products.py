from fastapi import APIRouter, Depends
from model import Product
from auth  import get_current_user
from database import get_session

router = APIRouter(prefix="/products")

@router.post("/")
def create_product(name: str, price: float, user=Depends(get_current_user), session=Depends(get_session)):
    product = Product(name=name, price=price, user_id=user.id)
    session.add(product)
    session.commit()
    return product