from fastapi import APIRouter, HTTPException, Depends
from pymongo.collection import Collection
from utils.database import db

router = APIRouter()
users_collection: Collection = db["users"]

@router.post("/link")
async def link_id(email: str, external_id: str):
    result = users_collection.update_one({"email": email}, {"$set": {"external_id": external_id}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "ID linked successfully"}
