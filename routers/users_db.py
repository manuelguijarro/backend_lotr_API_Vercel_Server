from fastapi import APIRouter,HTTPException
from db.models.user import User
from db.client import db_users_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId


router = APIRouter(
  prefix="/users",
  tags=["users"]
)



@router.get("/")
async def get_users():
  try:
    users = db_users_client.user.find()
    return users_schema(users)
  except:
    raise HTTPException(status_code=404, detail="Users not found")

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