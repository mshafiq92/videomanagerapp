from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
import os
from app.routes import video_routes
from app.dbConnection import initialize_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting Video Manager Application...")
    await initialize_database()
    print("✅ Application startup complete!")
    yield
    # Shutdown (cleanup if needed)
    print("🛑 Shutting down Video Manager Application...")

# FastAPI app with enhanced metadata
app = FastAPI(
    title="Video Manager Dashboard",
    description="""
    🎬 **Video Manager Dashboard** - A modern web application for managing your video collection.
    
    ## Features
    * 📂 Browse and list all videos
    * ➕ Add new videos with metadata
    * ✏️ Edit existing video information  
    * 🗑️ Delete videos from collection
    * 🔍 Search and filter capabilities
    * 📱 Responsive design for all devices
    
    ## Tech Stack
    * **Backend**: FastAPI + Python
    * **Database**: MongoDB Atlas
    * **Frontend**: HTML5 + CSS3 + JavaScript
    * **Deployment**: Docker + Docker Compose
    """,
    version="2.0.0",
    contact={
        "name": "Video Manager Support",
        "email": "support@videomanager.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Static files (CSS/JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Health check endpoint for Docker
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring and Docker health checks"""
    return {
        "status": "healthy",
        "service": "Video Manager Dashboard",
        "version": "2.0.0"
    }

# Index route
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Include video routes
app.include_router(video_routes.router)
