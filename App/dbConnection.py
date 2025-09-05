import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

try:
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    client = AsyncIOMotorClient(mongo_uri)
    print("✅ Database connected successfully!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")

# Database and collection
db = client["ytmanager"]
video_collection = db["videos"]
