from motor.motor_asyncio import AsyncIOMotorClient
from Config import Config

client = AsyncIOMotorClient(Config.db_uri)
print(client)