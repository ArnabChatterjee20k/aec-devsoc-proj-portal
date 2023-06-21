from beanie import Document, Link , WriteRules , BackLink
from beanie.operators import Push
from pydantic import Field

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from typing import Optional
import asyncio
from bson import ObjectId
from pprint import pprint

class Paint(Document):
    color:str = "red"

class House(Document):
    name: str
    door: Optional[Link["Door"]]

class Door(Document):
    height: int = 2
    width: int = 1
    paint : Optional[list[Link[Paint]]]
    house:BackLink[House] = Field(original_field="door")


async def example():
    client = AsyncIOMotorClient("mongodb://localhost:27017/")
    await init_beanie(database=client.devsoc, document_models=[Door,House,Paint])
    # for fetching backlinks as well we need to use fetch_links
    door = await Door.find_one({"_id":ObjectId("64916134562a0d1fdd041df1")},fetch_links=True)
    paint = Paint()
    new_paint = await paint.save()
    door.paint.append(new_paint)
    await door.save()
    print(len(door.paint))
asyncio.run(example())