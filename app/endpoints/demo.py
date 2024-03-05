from typing import Annotated
from fastapi import Depends, APIRouter
from app.services.demo import create_user, get_user, update_user, delete_user, all_users
from app.models import User

router = APIRouter()

@router.post("/user")
async def create_user_endpoint(request: Annotated[User, Depends()]):
    """
    Creates a user.

    Args:
    - request (Annotated[User, Depends()]): Request model containing user ID and name.

    Returns:
    - dict: Response message and user details.
    """
    return create_user(request.id, request.name)

@router.get("/user/{user_id}")
async def get_user_endpoint(request: Annotated[User, Depends()]):
    """
    Retrieves user details.

    Args:
    - request (Annotated[User, Depends()]): ID of the user to retrieve.

    Returns:
    - dict: User details.
    """
    return get_user(request.id)

@router.put("/user/{user_id}")
async def update_user_endpoint(request: Annotated[User, Depends()]):
    """
    Updates user details.

    Args:
    - request (Annotated[User, str, Depends()]): ID of the user to update and new name.


    Returns:
    - dict: Response message and updated user details.
    """
    return update_user(request.id, request.name)

@router.delete("/user/{user_id}")
async def delete_user_endpoint(request: Annotated[User, Depends()]):
    """
    Deletes a user.

    Args:
    - request (Annotated[User, Depends()]): ID of the user to delete.

    Returns:
    - dict: Response message.
    """
    return delete_user(request.id)

@router.get("/users")
async def all_users_endpoint():
    """
    Retrieves all users.

    Returns:
    - dict: User details.
    """
    return all_users()

