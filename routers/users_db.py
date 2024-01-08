from fastapi import APIRouter,HTTPException


router = APIRouter(
  prefix="/users",
  tags=["users"]
)

@router.get("/")
async def get_users():
  return {"message": "Hello from users db"}

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