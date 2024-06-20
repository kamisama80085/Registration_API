from fastapi import APIRouter, HTTPException, Depends
from pymongo.collection import Collection
from models.user_model import User
from util.database  import db
from util.security import hash_password, verify_password

router = APIRouter()

users_collection: Collection = db["users"]

@router.post("/register")
async def register_user(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    user.password = hash_password(user.password)
    users_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
async def login_user(email: str, password: str):
    user = users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}
