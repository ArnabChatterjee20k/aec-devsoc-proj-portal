from fastapi import APIRouter, Depends
from api.v1.utils.JWTBearer import JWTBearer
from api.v1.utils.user_utils import get_user_profile, edit_profile
from api.v1.Schemas.Profile import ProfileEdit

router = APIRouter(dependencies=[Depends(JWTBearer())])


@router.get("/")
async def user_profile(token: str = Depends(JWTBearer())):
    data = token.get("sub")
    email = data.get("email")
    return await get_user_profile(email=email)


@router.put("/:id")
async def update_user(id: str, data: ProfileEdit, token: str = Depends(JWTBearer())):
    data = token.get("sub")
    email = data.get("email")
    await edit_profile(data=data, profile_id=id, email=email)
    return {"message": "sucess"}
