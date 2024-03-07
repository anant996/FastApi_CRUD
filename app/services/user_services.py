from fastapi import HTTPException, status
from app.utils.dummy_db import demo_db
from pydantic import EmailStr

async def create_user(user_id:int, name:str, email:EmailStr):
    # if user_id in demo_db:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    for user in demo_db.values():
        if user['email'] == email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    else:
        demo_db[user_id] = {"id":user_id, "name": name, "email":email}
        return {"message": "User created successfully", "user": demo_db[user_id]}, status.HTTP_201_CREATED

async def get_user(user_id:int):
    if user_id in demo_db:
        return demo_db[user_id], status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
async def update_user(user_id:int, name:str, email: EmailStr):
    if user_id in demo_db:
        for user in demo_db.values():
            if user['email'] == email:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
            else:
                demo_db[user_id]['name'] = name
                demo_db[user_id]['email'] = email 
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

async def get_users_by_name(name:str):
    matches = [user for user in demo_db.values() if name in user['name']]
    if not matches:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found with names containing 'nt'")
    return matches, status.HTTP_200_OK

async def get_user_by_nameemail(name:str, email:EmailStr):
    match = [user for user in demo_db.values() if user['name'] == name and user['email'] == email]
    if not match:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found with given name and email")
    else:
        return match, status.HTTP_200_OK