from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Optional

router = APIRouter()


products_db = {
    1: {"name": "Product1", "price": 10.0},
    2: {"name": "Product2", "price": 20.0}
}
class Response(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[Any] = None

class Product(BaseModel):
    name: str
    price: float


@router.get("/{product_id}", response_model=Response)
async def read_product(product_id: int):
    if product_id not in products_db:
        return Response(status="fail", message="Product not found")
    return Response(status="ok", data=products_db[product_id])


@router.post("/", response_model=Response)
async def create_product(product: Product):
    try:
        new_product_id = max(products_db.keys()) + 1
        products_db[new_product_id] = product.dict()
        return Response(status="ok", data=product.dict())
    except Exception as e:
        return Response(status="exception", message=str(e))
