from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client[settings.DB_NAME]

async def init_db():
    """Initialize database indexes"""
    await db.entries.create_index([("createdAt", -1)])
    await db.entries.create_index([("userId", 1), ("createdAt", -1)])
    print("✓ Database indexes created")

