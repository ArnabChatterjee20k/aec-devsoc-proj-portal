from fastapi import APIRouter
from api.v1.utils.event_utils import create_new_event
from api.v1.Schemas.Event import EventSchema

router = APIRouter()

@router.post("/create")
async def create_event(data:EventSchema):
    id = await create_new_event(data.dict())
    return id