from pydantic import BaseModel
from typing import Union
class User(BaseModel):
  id: Union[str, None]
  username: str
  email: str
  password: str
  created_at: Union[str, None]
  