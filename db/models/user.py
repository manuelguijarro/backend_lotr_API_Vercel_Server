from pydantic import BaseModel

class User(BaseModel):
  id: str | None
  username: str
  email: str
  password: str
  created_at: str | None
  