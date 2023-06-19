import secrets
import string
from api.v1.database.models import User
from .auth import create_access_token, verify_password
from fastapi import status, HTTPException
from api.v1.Schemas.Profile import Profile, ProfileEdit


async def register_user(user: dict) -> dict:
    profile_id = generate_profile_id(user["name"])
    user["profile_id"] = profile_id
    data = User(**user)
    user_object = await User.insert_one(data)
    return {"token": create_access_token({"email": user_object.email}), "profile_id": profile_id}


async def login_user(email, password) -> dict:
    user = await User.find_one(User.email == email)
    if user:
        hashed_password = user.password
        check = verify_password(password, hashed_password)
        if check:
            return {"token": create_access_token({"id": user.email}), "profile_id": user.profile_id}
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    raise HTTPException(status.HTTP_404_NOT_FOUND)


async def get_user_profile(email):

    user: User = await User.find_one(User.email == email).project(Profile)

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return user


async def edit_profile(email, profile_id, data: dict):
    query: dict = {"email": email, "profile_id": profile_id}

    # checking the data
    ProfileEdit(**data)
    user: User = await User.find_one(query)

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    user.update({"$set": data})
    print(user)


def generate_profile_id(name):
    unique_string = ''.join(secrets.choice(
        string.ascii_letters + string.digits) for _ in range(10))
    profile_id = f"{name}-{unique_string}"
    return profile_id
