from fastapi import APIRouter
from models.user import UserCreate
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users():
    return [
        {"id": 1, "name": "Juan"},
        {"id": 2, "name": "Ana"}
    ]
@router.post("/")
def create_user(user: UserCreate):
    return user

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
