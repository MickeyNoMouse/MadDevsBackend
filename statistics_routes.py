from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


statistics_db = {
    "total_users": 100,
    "total_orders": 50,
    "total_revenue": 500.0
}


class Statistics(BaseModel):
    total_users: int
    total_orders: int
    total_revenue: float


@router.get("/", response_model=Statistics)
async def get_statistics():
    return statistics_db
