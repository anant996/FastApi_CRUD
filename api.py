from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

demo_db={
    1:{
        "id":1,
        "name":"Anant"
    }
    
    }

class User(BaseModel):
    id:int = Field(..., gt=0, description="User ID must be greater than zero")
    name:str = Field(..., min_length=1, max_length=100, description="User name must be between 1 and 100 characters")
    
@app.post("/user")
async def create_user(user: User):
    if user.id in demo_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    else:
        demo_db[user.id] = {"id":user.id, "name": user.name}
        return {"message": "User created successfully", "user": demo_db[user.id]}, status.HTTP_201_CREATED
    
@app.get("/user/{user_id}")
async def get_user(user_id:int):
    if user_id in demo_db:
        return demo_db[user_id], status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.put("/user/{user_id}")
async def update_user(user_id:int, name:str):
    if user_id in demo_db:
        demo_db[user_id]["name"] = name
        return {"message": "User updated successfully", "user": demo_db[user_id]}, status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id:int):
    if user_id in demo_db:
        del demo_db[user_id]
        return {"message": "User deleted successfully"}, status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
@app.get("/users/")
async def all_users():
    if not demo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return demo_db, status.HTTP_200_OK
