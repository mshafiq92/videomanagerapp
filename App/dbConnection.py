import os
import asyncio
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection variables
client = None
db = None
video_collection = None

async def connect_to_database():
    """Establish connection to MongoDB Atlas with error handling and retry logic"""
    global client, db, video_collection
    
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    
    if not mongo_uri or mongo_uri == "mongodb://localhost:27017/":
        logger.error("❌ MONGO_URI not found in environment variables")
        return False
    
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            # Create client with timeout settings
            client = AsyncIOMotorClient(
                mongo_uri,
                serverSelectionTimeoutMS=5000,  # 5 second timeout
                connectTimeoutMS=10000,         # 10 second connection timeout
                socketTimeoutMS=10000           # 10 second socket timeout
            )
            
            # Test the connection
            await client.admin.command('ping')
            
            # Set up database and collection
            db = client["ytmanager"]
            video_collection = db["videos"]
            
            logger.info("✅ Database connected successfully!")
            return True
            
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            logger.warning(f"⚠️ Database connection attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                logger.info(f"🔄 Retrying in {retry_delay} seconds...")
                await asyncio.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            else:
                logger.error("❌ All database connection attempts failed")
                return False
        except Exception as e:
            logger.error(f"❌ Unexpected database connection error: {e}")
            return False
    
    return False

async def check_database_health():
    """Check if database connection is healthy"""
    try:
        if client is None:
            return False
        await client.admin.command('ping')
        return True
    except Exception as e:
        logger.error(f"❌ Database health check failed: {e}")
        return False

def get_video_collection():
    """Get video collection with connection check"""
    if video_collection is None:
        logger.error("❌ Database not connected. Call connect_to_database() first.")
        return None
    return video_collection

# Initialize connection (will be called from main.py)
async def initialize_database():
    """Initialize database connection on startup"""
    success = await connect_to_database()
    if not success:
        logger.warning("⚠️ Application starting without database connection")
    return success
