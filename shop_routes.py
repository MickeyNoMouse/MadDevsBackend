from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Optional

router = APIRouter()


shops_db = {
    1: {"name": "Shop1", "location": "Location1"},
    2: {"name": "Shop2", "location": "Location2"}
}

class Response(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[Any] = None

class Shop(BaseModel):
    name: str
    location: str


@router.get("/{shop_id}", response_model=Response)
async def read_shop(shop_id: int):
    if shop_id not in shops_db:
        return Response(status="fail", message="Shop not found")
    return Response(status="ok", data=shops_db[shop_id])


@router.post("/", response_model=Response)
async def create_shop(shop: Shop):
    try:
        new_shop_id = max(shops_db.keys()) + 1
        shops_db[new_shop_id] = shop.dict()
        return Response(status="ok", data=shop.dict())
    except Exception as e:
        return Response(status="exception", message=str(e))
