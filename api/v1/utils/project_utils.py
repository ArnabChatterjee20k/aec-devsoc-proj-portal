from api.v1.database.models.Project import Project
from api.v1.database.models.User import User
from api.v1.Schemas.Project import ProjectDetails
from beanie import PydanticObjectId
from bson import ObjectId, errors
from fastapi import HTTPException, status

async def create_project(data: dict):
    details = ProjectDetails(**data).dict()
    new_project = Project(**details)
    await new_project.save()
    return new_project.id


async def get_all_projects():
    return await Project.find(fetch_links=True).project(ProjectDetails).to_list()


async def get_project_by_id(id: PydanticObjectId):
    return await Project.find_one({"_id": ObjectId(id)})


async def get_project_by_profile_id(id: str):
    return await Project.find({"owner_id": id}).project(ProjectDetails).to_list()


async def get_project_of_a_user(user_id, project_id):
    try:
        return await Project.find_one({"owner_id": user_id, "_id": ObjectId(project_id)}).project(ProjectDetails)
    except errors.InvalidId as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
