from fastapi import status,HTTPException,Depends
from api.v1.utils.JWTBearer import JWTBearer
from api.v1.database.models import User

async def getUserIdByEmail(token:str=Depends(JWTBearer())):
    email = token.get("sub").get("email")
    user = await User.find_one(User.email == email)
    
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return user.profile_id