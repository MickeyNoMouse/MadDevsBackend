from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


shops_db = {
    1: {"name": "Shop1", "location": "Location1"},
    2: {"name": "Shop2", "location": "Location2"}
}


class Shop(BaseModel):
    name: str
    location: str


@router.get("/{shop_id}", response_model=Shop)
async def read_shop(shop_id: int):
    if shop_id not in shops_db:
        raise HTTPException(status_code=404, detail="Shop not found")
    return shops_db[shop_id]


@router.post("/", response_model=Shop)
async def create_shop(shop: Shop):
    new_shop_id = max(shops_db.keys()) + 1
    shops_db[new_shop_id] = shop
    return shop
