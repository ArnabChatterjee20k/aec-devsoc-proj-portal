from beanie import  Link , Document , PydanticObjectId
from .User import User
from typing import Optional , List
from pydantic import BaseModel , HttpUrl , Field
from datetime import date,time,datetime

from api.v1.database.models.EventsParticipants import EventsParticipants

class Event(Document):
    name:str
    description:str # markdown
    start:str
    end:str
    start_time:str
    end_time:str
    banner:HttpUrl
    details_fields : Optional[list[str]]
    participants : Optional[list[Link[EventsParticipants]]] = []

    # class Settings:
    #     bson_encoders = {
    #         "start_time": lambda dt: datetime(year=dt.year, month=dt.month, day=dt.day, hour=0, minute=0, second=0),
    #         "end_time": lambda dt: datetime(year=dt.year, month=dt.month, day=dt.day, hour=0, minute=0, second=0),
    #     }
