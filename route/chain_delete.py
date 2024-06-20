from fastapi import APIRouter, HTTPException
from util.database import db

router = APIRouter()
users_collection = db["users"]
orders_collection = db["orders"]

@router.delete("/user")
async def delete_user(email: str):
    user = users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    orders_collection.delete_many({"user_id": user["_id"]})
    users_collection.delete_one({"email": email})
    
    return {"message": "User and associated data deleted successfully"}
