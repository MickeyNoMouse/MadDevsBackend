from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Optional

router = APIRouter()


brands_db = {
    1: {"name": "Brand1", "description": "Description1"},
    2: {"name": "Brand2", "description": "Description2"}
}
class Response(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[Any] = None

class Brand(BaseModel):
    name: str
    description: str


@router.get("/{brand_id}", response_model=Response)
async def read_brand(brand_id: int):
    if brand_id not in brands_db:
        return Response(status="fail", message="Brand not found")
    return Response(status="ok", data=brands_db[brand_id])


@router.post("/", response_model=Response)
async def create_brand(brand: Brand):
    try:
        new_brand_id = max(brands_db.keys()) + 1
        brands_db[new_brand_id] = brand.dict()
        return Response(status="ok", data=brand.dict())
    except Exception as e:
        return Response(status="exception", message=str(e))

