from motor.motor_asyncio import AsyncIOMotorClient 
from Config import Config
from beanie import init_beanie
from .models import models


async def init_db():
    client = AsyncIOMotorClient(Config.db_uri)
    await init_beanie(database=client.devsoc,document_models=models)
