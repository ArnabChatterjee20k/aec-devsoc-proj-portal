from beanie import Document, Link , BackLink
from .Project import Project
from typing import Optional


class User(Document):
    name: str
    profile_id: str
    email: str
    profession: list[str]
    institution: str

    password: str  # hashed()

    # automatically created
    # contributed: Optional[Link[]]