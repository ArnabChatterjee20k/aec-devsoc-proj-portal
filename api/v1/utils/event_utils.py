from api.v1.database.models.Event import Event
from api.v1.Schemas.Event import EventSchema

async def create_new_event(data:dict):
    submitted_event = EventSchema(**data).dict()
    new_event = Event(**submitted_event)
    await new_event.insert()
    print(new_event)
    return 12