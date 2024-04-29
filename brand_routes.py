from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


brands_db = {
    1: {"name": "Brand1", "description": "Description1"},
    2: {"name": "Brand2", "description": "Description2"}
}


class Brand(BaseModel):
    name: str
    description: str


@router.get("/{brand_id}", response_model=Brand)
async def read_brand(brand_id: int):
    if brand_id not in brands_db:
        raise HTTPException(status_code=404, detail="Brand not found")
    return brands_db[brand_id]


@router.post("/", response_model=Brand)
async def create_brand(brand: Brand):
    new_brand_id = max(brands_db.keys()) + 1
    brands_db[new_brand_id] = brand
    return brand
