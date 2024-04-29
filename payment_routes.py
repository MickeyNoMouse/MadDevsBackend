from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


payments_db = {
    1: {"amount": 100.0, "status": "completed"},
    2: {"amount": 50.0, "status": "pending"}
}


class Payment(BaseModel):
    amount: float
    status: str

@router.get("/{payment_id}", response_model=Payment)
async def read_payment(payment_id: int):
    if payment_id not in payments_db:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payments_db[payment_id]

@router.post("/", response_model=Payment)
async def create_payment(payment: Payment):
    new_payment_id = max(payments_db.keys()) + 1
    payments_db[new_payment_id] = payment
    return payment
