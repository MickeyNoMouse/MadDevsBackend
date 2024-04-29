from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


products_db = {
    1: {"name": "Product1", "price": 10.0},
    2: {"name": "Product2", "price": 20.0}
}


class Product(BaseModel):
    name: str
    price: float


@router.get("/{product_id}", response_model=Product)
async def read_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]


@router.post("/", response_model=Product)
async def create_product(product: Product):
    new_product_id = max(products_db.keys()) + 1
    products_db[new_product_id] = product
    return product
