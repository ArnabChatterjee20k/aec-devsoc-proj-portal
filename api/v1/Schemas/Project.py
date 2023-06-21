from typing import Optional
from pydantic import BaseModel, Field
from beanie import PydanticObjectId
from enum import Enum


class LinkType(str, Enum):
    website = "website"
    github = "github"


class SourceLink(BaseModel):
    link: str
    type: LinkType


class ProjectDetails(BaseModel):
    # alias is required to identify the _id
    id: Optional[PydanticObjectId] = Field(alias='_id')
    owner_id: str
    title: str
    description: str
    links: SourceLink
    pinned: bool

    # Contributors
