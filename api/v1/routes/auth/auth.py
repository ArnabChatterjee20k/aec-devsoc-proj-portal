from fastapi import APIRouter, Depends
from api.v1.utils.JWTBearer import JWTBearer
from ...Schemas.Auth import Register , Login
from api.v1.utils.auth import get_password_hash, verify_password
from api.v1.utils.user_utils import register_user , login_user
from api.v1.dependencies.userExists import userExists

router = APIRouter()

@router.post("/")
async def register(user: Register = Depends(userExists)):
    hashed_password = get_password_hash(user.password)
    user_data = user.dict()
    user_data["password"] = hashed_password

    return await register_user(user_data)


@router.post("/login")
async def login(data:Login):
    user_details = Login(**data.dict())
    return await login_user(user_details.email,user_details.password)
