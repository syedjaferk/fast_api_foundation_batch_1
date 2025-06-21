from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING

MONGO_URI = "mongodb://mongo:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client.todo_db
collection = db.todos

async def create_index():
    await collection.create_index([("title", ASCENDING)], unique=False)
