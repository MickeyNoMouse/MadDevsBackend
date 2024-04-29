from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Optional

router = APIRouter()


payments_db = {
    1: {"amount": 100.0, "status": "completed"},
    2: {"amount": 50.0, "status": "pending"}
}

class Response(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[Any] = None

class Payment(BaseModel):
    amount: float
    status: str

@router.get("/{payment_id}", response_model=Response)
async def read_payment(payment_id: int):
    if payment_id not in payments_db:
        return Response(status="fail", message="Payment not found")
    return Response(status="ok", data=payments_db[payment_id])


@router.post("/", response_model=Response)
async def create_payment(payment: Payment):
    try:
        new_payment_id = max(payments_db.keys()) + 1
        payments_db[new_payment_id] = payment.dict()
        return Response(status="ok", data=payment.dict())
    except Exception as e:
        return Response(status="exception", message=str(e))

