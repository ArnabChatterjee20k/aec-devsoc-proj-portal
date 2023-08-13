from api.v1.database.models.Event import Event
from api.v1.Schemas.Event import EventSchema , FieldPool
from api.v1.Schemas.EventParticipant import EventsParticipantsSchema
from api.v1.database.models.EventsParticipants import EventsParticipants

from typing import Optional
from beanie import PydanticObjectId
from pydantic import Field
from bson import ObjectId
from fastapi import HTTPException , status
class EventShowSchema(EventSchema):
    id: Optional[PydanticObjectId] = Field(alias='_id')


async def create_new_event(data:dict):
    submitted_event = EventSchema(**data).dict()
    new_event = Event(**submitted_event)
    doc = await new_event.insert()
    return doc

async def get_all_events():
    return await Event.find().project(EventShowSchema).to_list()

async def get_event_by_id(id:str,get_nested_data=False):
    return await Event.find_one({"_id":ObjectId(id)},fetch_links=get_nested_data)

async def participate_in_event(user_id:str,event_id:str,data:EventsParticipantsSchema):
    # print(user_id,event_id,data)
    event = await get_event_by_id(event_id)
    print(event)
    if not event:
        raise HTTPException(status_code=404)
    await validate_participants(event,data,user_id,event_id)
    participant = EventsParticipants(event_id=event_id,participant_id=user_id,details=data)
    saved_data = await participant.save()
    event.participants.append(saved_data)
    await event.save()

async def validate_participants(event:Event,data:EventsParticipantsSchema,user_id,event_id):
    isUserPresent = await EventsParticipants.find_one({"participant_id":user_id,"event_id":event_id})
    if isUserPresent:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    print(data)
    print(event.details_fields)
    submitted_fields = data
    required_fields = event.details_fields
    fields_present = submitted_fields.keys()

    for field in required_fields:
        if field not in fields_present:
            print(field)
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail="All fields not present")

async def get_participants_by_id(event_id:str):
    event = await get_event_by_id(event_id)
    return event.participants

async def get_winner_by_id(event_id:str):
    event = await get_event_by_id(event_id,get_nested_data=True)
    winner = event.winner
    return winner
