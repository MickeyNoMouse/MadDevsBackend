from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


users_db = {
    1: {"username": "user1", "email": "user1@example.com"},
    2: {"username": "user2", "email": "user2@example.com"}
}


class User(BaseModel):
    username: str
    email: str


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]


@router.post("/", response_model=User)
async def create_user(user: User):
    new_user_id = max(users_db.keys()) + 1
    users_db[new_user_id] = user
    return user
