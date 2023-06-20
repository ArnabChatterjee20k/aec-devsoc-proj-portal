import pytest
from api.v1.database.models.Project import Project
from api.v1.database.models.User import User
from beanie import PydanticObjectId
from api.v1.utils.project_utils import create_project, get_all_projects, get_project_by_id, get_project_by_profile_id, get_project_of_a_user
from api.v1.utils.user_utils import get_user_profile
from api.v1.utils.auth import decode_access_token
from api.v1.database.db import init_db
from api.v1.utils.user_utils import login_user
from bson import ObjectId

test_user_details = {
    "email": "test@example.com",
    "phone_number": "1234567890",
    "name": "John Doe",
    "profession": ["Engineer"],
    "institution": "ABC University",
    "password": "password",
}


@pytest.mark.asyncio
async def test_create_project():
    await init_db()
    data = {
        "owner_id": 12,
        "title": "Project A",
        "description": "This is project A",
        "links": {
            "link": "https://example.com",
            "type": "website"
        },
        "pinned": True
    }
    project_id = await create_project(data)
    assert isinstance(project_id, PydanticObjectId)


@pytest.mark.asyncio
async def test_get_all_projects():
    await init_db()
    projects = await get_all_projects()
    assert isinstance(projects, list)


@pytest.mark.asyncio
async def test_get_project_by_id():
    await init_db()
    project = Project(title="Project B", description="This is project B",
                      owner_id=12, links={"link": "http://google.com", "type": "website"}, pinned=False)
    await project.save()
    retrieved_project = await get_project_by_id(project.id)
    assert retrieved_project == project


@pytest.mark.asyncio
async def test_get_project_by_profile_id():
    await init_db()
    owner_id = "user123"
    projects = await get_project_by_profile_id(owner_id)
    assert isinstance(projects, list)


@pytest.mark.asyncio
async def test_get_project_of_a_user():
    await init_db()
    user_id = "user123"
    project_id = ObjectId()
    project = await get_project_of_a_user(user_id, project_id)
    assert project is None
