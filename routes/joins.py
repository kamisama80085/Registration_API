from fastapi import APIRouter, HTTPException
from utils.database import db

router = APIRouter()
users_collection = db["users"]
orders_collection = db["orders"]

@router.get("/user-orders")
async def get_user_orders(email: str):
    user = users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    orders = list(orders_collection.find({"user_id": user["_id"]}))
    user["orders"] = orders
    return user
