from fastapi import APIRouter
from api.v1.utils.event_utils import create_new_event , get_all_events,get_event_by_id
from api.v1.Schemas.Event import EventSchema

router = APIRouter()

@router.get("/")
async def get_events():
    return await get_all_events()

@router.post("/create")
async def create_event(data:EventSchema):
    id = await create_new_event(data.dict())
    return id

@router.get("/:id")
async def get_event(id:str):
    return await get_event_by_id(id)