from fastapi import APIRouter , Depends , Response
from api.v1.utils.event_utils import create_new_event , get_all_events,get_event_by_id , participate_in_event
from api.v1.Schemas.Event import EventSchema
from api.v1.utils.JWTBearer import JWTBearer
from api.v1.dependencies.getUserIdByEmail import getUserIdByEmail
from typing import Union
from api.v1.Schemas.Event import FieldPool

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

@router.post("/event_id/participate",dependencies=[Depends(JWTBearer())])
async def participate(data:dict[FieldPool, Union[str, dict]],event_id:str,user_id: str = Depends(getUserIdByEmail)):
    await participate_in_event(user_id,event_id,data)
    return {"message": "Participant Added","status":"success"}
