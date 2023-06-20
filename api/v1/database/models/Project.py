from beanie import Document, Link, PydanticObjectId
from typing import Optional
from pydantic import BaseModel
from enum import Enum


class LinkType(str, Enum):
    website = "website"
    github = "github"


class SourceLink(BaseModel):
    link: str
    type: LinkType


class Project(Document):
    owner_id: str
    title: str
    description: str
    links: SourceLink
    pinned: bool

    # Contributors