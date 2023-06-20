import pytest
from api.v1.database.models import User
from api.v1.Schemas.Profile import Profile, ProfileEdit
from api.v1.utils.user_utils import (
    register_user,
    login_user,
    get_user_profile,
    edit_profile,
    generate_profile_id,
)
from api.v1.database.db import init_db

@pytest.fixture
def user_data():
    return {
        "email": "test@example.com",
        "phone_number": "1234567890",
        "name": "John Doe",
        "profession": ["Engineer"],
        "institution": "ABC University",
        "password": "password",
    }


@pytest.fixture
def registered_user(user_data, monkeypatch):
    async def mock_insert_one(data):
        user_object = User(**data)
        user_object.email = data["email"]
        user_object.profile_id = generate_profile_id(data["name"])
        return user_object

    monkeypatch.setattr(User, "insert_one", mock_insert_one)
    return user_data


@pytest.mark.asyncio
async def test_register_user(registered_user):
    await init_db()
    result = await register_user(registered_user)
    assert "token" in result
    assert "profile_id" in result


@pytest.mark.asyncio
async def test_login_user(registered_user):
    await init_db()
    email = registered_user["email"]
    password = registered_user["password"]

    result = await login_user(email, password)
    assert "token" in result
    assert "profile_id" in result


@pytest.mark.asyncio
async def test_get_user_profile(registered_user):
    await init_db()
    email = registered_user["email"]

    result = await get_user_profile(email)
    assert isinstance(result, Profile)


@pytest.mark.asyncio
async def test_edit_profile(registered_user):
    await init_db()
    email = registered_user["email"]
    user = await get_user_profile(email)
    data = {"name": "Updated Name"}

    await edit_profile(email, user.profile_id, data)

    result = await get_user_profile(email)
    assert result.name == "Updated Name"


def test_generate_profile_id():
    name = "John Doe"
    profile_id = generate_profile_id(name)
    assert profile_id.startswith(name)
    assert len(profile_id) == len(name) + 11  # Name length + length of unique string
