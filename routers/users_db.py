from fastapi import APIRouter,HTTPException
from db.models.user import User
from db.client import db_users_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId
from typing import Union


router = APIRouter(
  prefix="/users",
  tags=["users"]
)

#functions
def search_user(key: str, value:Union[str, None]):
  try:
    user = db_users_client.user.find_one({key: value})
    return User(**user_schema(user))
  except:
    return {"error": "user not found"}
  
def get_user_object(key: str, value: Union[str, None]):
  try:
    user = db_users_client.user.find_one({key: value})
    return User(**user_schema(user))
  except:
    return {"error": "user not found"}

#CRUD USERS


@router.get("/")
async def get_users():
  try:
    users = db_users_client.user.find()
    return users_schema(users)
  except:
    raise HTTPException(status_code=404, detail="Users not found")

@router.get("/{id}", response_model=User)
async def get_user(id : str):
  try:
    return search_user("_id", ObjectId(id))
  except:
    raise HTTPException(status_code=404, detail="user not found")
  

@router.post("/", response_model=User, status_code=201)
async def create_user(user : User):
  if type(search_user("email", user.email)) == User:
    raise HTTPException(status_code=406, detail="user already exists")
  try:
    user_dict = dict(user)
    del user_dict['id']
    #primero lo guardo en la base de datos y obtengo el id despues.
    id = db_users_client.user.insert_one(user_dict).inserted_id
    new_user = user_schema(db_users_client.user.find_one({"_id": id}))
    return User(**new_user)#y devolvemos el nuevo usuario creado
  except:
    raise HTTPException(status_code=400, detail="error creating user")
 
@router.put("/{username}")
async def update_user(username: str):
  return {"message": "Hello from update users db", "username": username}

@router.delete("/{id}")
async def delete_user(id: str):
  return {"message": "Hello from delete users db", "id": id}