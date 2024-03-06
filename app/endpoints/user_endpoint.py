from typing import Annotated
from fastapi import Depends, APIRouter
from app.services.user_services import create_user, get_user, update_user, delete_user, all_users
from app.models import User

router = APIRouter()

@router.get("/")
async def welcome():
    """
    Home Page.

    Returns:
    - str: Welcome message with URL for testing.
    """
    return "Welcome to the homepage. Go to [Swagger UI](http://127.0.0.1:8000/docs) for testing."

@router.post("/user")
async def create_user_endpoint(request: Annotated[User, Depends()]):
    """
    Creates a user.

    Args:
    - request (Annotated[User, Depends()]): Request model containing user ID and name.

    Returns:
    - dict: Response message and user details.
    """
    return await create_user(request.id, request.name)

@router.get("/user/{user_id}")
async def get_user_endpoint(user_id:int):
    """
    Retrieves user details.

    Args:
    - user_id: ID of the user to retrieve.

    Returns:
    - dict: User details.
    """
    return await get_user(user_id)

@router.put("/user/{user_id}")
async def update_user_endpoint(request: Annotated[User, Depends()]):
    """
    Updates user details.

    Args:
    - request (Annotated[User, str, Depends()]): ID of the user to update and new name.

    Returns:
    - dict: Response message and updated user details.
    """
    return await update_user(request.id, request.name)

@router.delete("/user/{user_id}")
async def delete_user_endpoint(user_id:int):
    """
    Deletes a user.

    Args:
    - user_id: ID of the user to delete.

    Returns:
    - dict: Response message.
    """
    return await delete_user(user_id)

@router.get("/users")
async def all_users_endpoint():
    """
    Retrieves all users.

    Returns:
    - dict: User details.
    """
    return await all_users()

