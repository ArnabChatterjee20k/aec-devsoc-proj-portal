from fastapi import APIRouter, Depends
from api.v1.utils.JWTBearer import JWTBearer
router = APIRouter(dependencies=[Depends(JWTBearer())])


@router.get("/:id")
def get_user_profile(id: str):
    return id


@router.put("/")
def update_user():
    return "User"