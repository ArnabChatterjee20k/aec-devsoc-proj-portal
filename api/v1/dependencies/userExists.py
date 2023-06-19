from fastapi import status, Request, HTTPException
from pydantic import EmailStr
from api.v1.database.models import User
from api.v1.Schemas.Auth import Register


async def userExists(request: Register):
    data = request.dict()
    email = data.get("email")
    print(email)
    user = await User.find_one(User.email == email)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={
                            "message": "email already exists"})
    return request
