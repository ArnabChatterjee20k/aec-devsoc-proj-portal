from fastapi import status, HTTPException, Depends
from api.v1.utils.JWTBearer import JWTBearer
from api.v1.Schemas.Project import ProjectDetails
from api.v1.database.models import User


async def isOwner(data: ProjectDetails, token: str = Depends(JWTBearer())):
    data = ProjectDetails(**data.dict())
    
    email = token.get("sub").get("email")
    print(token)
    print(email)
    user = await User.find_one(User.email == email)
    
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    if user and user.profile_id != data.owner_id:
        raise HTTPException(status.HTTP_403_FORBIDDEN)

    return user, data.dict()
