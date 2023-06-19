from pydantic import BaseModel, EmailStr
from typing import Optional


class Profile(BaseModel):
    email: EmailStr
    profile_id: str
    name: str
    profession: list[str]
    institution: str
    contributed: list[str] | None


class ProfileEdit(BaseModel):
    email: Optional[EmailStr]
    name: Optional[str]
    profession: Optional[list[str]]
    institution: Optional[str]
    contributed: Optional[list[str]]
