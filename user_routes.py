from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Optional

router = APIRouter()


users_db = {
    1: {"username": "user1", "email": "user1@example.com"},
    2: {"username": "user2", "email": "user2@example.com"}
}

class Response(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[Any] = None

class User(BaseModel):
    username: str
    email: str


@router.get("/{user_id}", response_model=Response)
async def read_user(user_id: int):
    if user_id not in users_db:
        return Response(status="fail", message="User not found")
    user_data = users_db[user_id]
    return Response(status="ok", data=user_data)


@router.post("/", response_model=Response)
async def create_user(user: User):
    new_user_id = max(users_db.keys()) + 1
    users_db[new_user_id] = user
    return Response(status="ok", data=user)
