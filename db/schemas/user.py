def user_schema(user) -> dict:
  return {
    "id": str(user["_id"]),
    "username": user["username"],
    "email": user["email"],
    "created_at": user["created_at"]
  }

def users_schema(users) -> list:
  return [user_schema(user) for user in users]