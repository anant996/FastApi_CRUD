from fastapi import HTTPException, status
from app.utils.dummy_db import demo_db

async def create_user(user_id:int, name:str):
    if user_id in demo_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    else:
        demo_db[user_id] = {"id":user_id, "name": name}
        return {"message": "User created successfully", "user": demo_db[user_id]}, status.HTTP_201_CREATED

async def get_user(user_id:int):
    if user_id in demo_db:
        return demo_db[user_id], status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
async def update_user(user_id:int, name:str):
    if user_id in demo_db:
        demo_db[user_id]["name"] = name
        return {"message": "User updated successfully", "user": demo_db[user_id]}, status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
async def delete_user(user_id:int):
    if user_id in demo_db:
        del demo_db[user_id]
        return {"message": "User deleted successfully"}, status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
async def all_users():
    if not demo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return demo_db, status.HTTP_200_OK


