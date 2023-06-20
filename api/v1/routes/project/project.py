from fastapi import APIRouter, Depends, HTTPException, status
from .ProjectOwnerSchema import ProjectOwnerSchema
from api.v1.utils.JWTBearer import JWTBearer
from api.v1.Schemas.Project import ProjectDetails
from api.v1.dependencies.isOwner import isOwner
from api.v1.utils.project_utils import create_project, get_all_projects, get_project_by_id
from beanie import PydanticObjectId

router = APIRouter()


@router.get("/all")
async def projects():
    return await get_all_projects()


@router.get("/:id")
async def single_project(id: PydanticObjectId):
    PydanticObjectId(**id)
    return await get_project_by_id(id)


@router.post("/create", dependencies=[Depends(JWTBearer())])
async def register_project(data: tuple = Depends(isOwner)):
    user, details = data
    proj_id = await create_project(owner=user, data=details)
    response = {"message": "project_created"}
    if proj_id:
        return response
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Some problem occured")


@router.put("/:id", dependencies=[Depends(JWTBearer())])
def update_project(id: PydanticObjectId, data: tuple = Depends(isOwner)):
    PydanticObjectId(**id)
    pass