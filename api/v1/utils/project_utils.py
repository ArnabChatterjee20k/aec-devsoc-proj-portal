from api.v1.database.models import User
from api.v1.database.models.Project import Project
from api.v1.Schemas.Project import ProjectDetails, Contributor
from beanie import PydanticObjectId
from bson import ObjectId, errors
from fastapi import HTTPException, status


async def create_project(data: dict):
    details = ProjectDetails(**data).dict()
    new_project = Project(**details)
    await new_project.save()
    return new_project.id


async def get_all_projects():
    return await Project.find().project(ProjectDetails).to_list()


async def get_project_by_id(id: PydanticObjectId, contributors=False):
    return await Project.find_one({"_id": ObjectId(id)}, fetch_links=contributors)


async def get_project_by_profile_id(id: str):
    return await Project.find({"owner_id": id}).project(ProjectDetails).to_list()


async def get_project_of_a_user(user_id, project_id):
    try:
        return await Project.find_one({"owner_id": user_id, "_id": ObjectId(project_id)}).project(ProjectDetails)
    except errors.InvalidId as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)


async def get_contributors(project_id):
    try:
        project = await Project.find_one({"_id": ObjectId(project_id)}, fetch_links=True)
        return [Contributor(**item.dict()) for item in project.contributors]
    except errors.InvalidId as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)


async def add_contributors(project_id, user_email):
    user: User = await User.find_one(User.email == user_email)
    project: Project = await get_project_by_id(project_id, contributors=True)

    if not user or not project:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    if user not in project.contributors:
        project.contributors.append(user)
        await project.save()
    else:
        raise HTTPException(status.HTTP_403_FORBIDDEN)
