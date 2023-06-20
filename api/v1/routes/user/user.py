from fastapi import APIRouter, Depends
from api.v1.utils.JWTBearer import JWTBearer
from api.v1.utils.user_utils import get_user_profile, edit_profile
from api.v1.utils.project_utils import get_project_by_profile_id, get_project_of_a_user
from api.v1.Schemas.Profile import ProfileEdit

router = APIRouter()


@router.get("/", dependencies=[Depends(JWTBearer())])
async def user_profile(token: str = Depends(JWTBearer())):
    data = token.get("sub")
    email = data.get("email")
    return await get_user_profile(email=email)


@router.put("/:id", dependencies=[Depends(JWTBearer())])
async def update_user(id: str, data: ProfileEdit, token: str = Depends(JWTBearer())):
    data = token.get("sub")
    email = data.get("email")
    await edit_profile(data=data, profile_id=id, email=email)
    return {"message": "sucess"}


@router.get("/:user_id/projects/")
async def user_projects(user_id):
    return await get_project_by_profile_id(user_id)


@router.get("/:user_id/projects/:project_id")
async def user_projects(user_id, project_id):
    return await get_project_of_a_user(user_id, project_id)
