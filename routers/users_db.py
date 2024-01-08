from fastapi import APIRouter,HTTPException
from db.models.user import User
from db.client import db_users_client
from db.schemas.user import user_schema, users_schema
router = APIRouter(
  prefix="/users",
  tags=["users"]
)
usuario = User(id="1", username="johndoe", email="johndoe@me.com", password="secret", created_at="2021-01-01")
@router.get("/")
async def get_users():
  return {"message": "Hello from users db", "users": [usuario.dict()]}

@router.get("/{id}")
async def get_user(id: str):
  return {"message": "Hello from users db", "id": id}


@router.post("/")
async def create_user():
  return {"message": "Hello from create users db"}

@router.put("/{username}")
async def update_user(username: str):
  return {"message": "Hello from update users db", "username": username}

@router.delete("/{id}")
async def delete_user(id: str):
  return {"message": "Hello from delete users db", "id": id}