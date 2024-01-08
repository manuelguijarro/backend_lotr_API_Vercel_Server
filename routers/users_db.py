from fastapi import APIRouter,HTTPException


router = APIRouter(
  prefix="/users",
  tags=["users"]
)

@router.get("/")
async def get_users():
  return {"message": "Hello from users db"}