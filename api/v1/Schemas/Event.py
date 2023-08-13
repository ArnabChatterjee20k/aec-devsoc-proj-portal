from pydantic import BaseModel , HttpUrl
from datetime import date , time , datetime
from typing import Optional
from beanie import PydanticObjectId
from enum import Enum

class PublicProfile(str,Enum):
    linkedin = "linkedin"
    twitter = "twitter"
    github = "github"
    portfolio = "portfolio"
    stackoverflow = "stackoverflow"

class FieldPool(str,Enum):
    name = "name"
    team_name = "teamname"
    links = "links"
    email = "email"


class EventSchema(BaseModel):
    name:str
    description:str # markdown
    start:str
    end:str
    start_time:str
    end_time:str
    details_fields:list[FieldPool]
    banner:HttpUrl