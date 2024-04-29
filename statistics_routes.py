from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Optional

router = APIRouter()


statistics_db = {
    "total_users": 100,
    "total_orders": 50,
    "total_revenue": 500.0
}

class Response(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[Any] = None
class Statistics(BaseModel):
    total_users: int
    total_orders: int
    total_revenue: float


@router.get("/", response_model=Response)
async def get_statistics():
    try:
        return Response(status="ok", data=statistics_db)
    except Exception as e:
        return Response(status="exception", message=str(e))
