from api.v1.database.models.Event import Event
from api.v1.Schemas.Event import EventSchema
from typing import Optional
from beanie import PydanticObjectId
from pydantic import Field
from bson import ObjectId
class EventShowSchema(EventSchema):
    id: Optional[PydanticObjectId] = Field(alias='_id')


async def create_new_event(data:dict):
    submitted_event = EventSchema(**data).dict()
    new_event = Event(**submitted_event)
    doc = await new_event.insert()
    return doc

async def get_all_events():
    return await Event.find().project(EventShowSchema).to_list()

async def get_event_by_id(id:str):
    return await Event.find_one({"_id":ObjectId(id)})