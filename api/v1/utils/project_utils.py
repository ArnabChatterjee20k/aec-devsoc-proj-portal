from api.v1.database.models.Project import Project, SourceLink
from api.v1.database.models.User import User
from api.v1.Schemas.Project import ProjectDetails
from beanie import PydanticObjectId


async def create_project(owner: User, data: dict):
    details = ProjectDetails(**data).dict()
    new_project = Project(**details)
    await new_project.save()
    return new_project.id


async def get_all_projects():
    return await Project.find_all().to_list()


async def get_project_by_id(id: PydanticObjectId):
    return await Project.get(id)


async def get_project_by_profile_id(id: str):
    return await Project.find_all({"owner_id": id}).to_list()
