from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, HttpUrl, validator
from bson import ObjectId
from bson.errors import InvalidId
from pymongo.errors import PyMongoError
from datetime import datetime
import logging
from app.dbConnection import get_video_collection

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
logger = logging.getLogger(__name__)

# Pydantic models for validation
class VideoCreate(BaseModel):
    title: str
    description: str
    time: str
    url: HttpUrl
    
    @validator('title')
    def validate_title(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Title is required')
        if len(v) > 200:
            raise ValueError('Title must be less than 200 characters')
        return v.strip()
    
    @validator('description')
    def validate_description(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Description is required')
        if len(v) > 1000:
            raise ValueError('Description must be less than 1000 characters')
        return v.strip()
    
    @validator('time')
    def validate_time(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Time is required')
        return v.strip()

class VideoUpdate(BaseModel):
    title: str = None
    description: str = None
    time: str = None
    url: HttpUrl = None
    
    @validator('title')
    def validate_title(cls, v):
        if v is not None:
            if len(v.strip()) == 0:
                raise ValueError('Title cannot be empty')
            if len(v) > 200:
                raise ValueError('Title must be less than 200 characters')
            return v.strip()
        return v
    
    @validator('description')
    def validate_description(cls, v):
        if v is not None:
            if len(v.strip()) == 0:
                raise ValueError('Description cannot be empty')
            if len(v) > 1000:
                raise ValueError('Description must be less than 1000 characters')
            return v.strip()
        return v
    
    @validator('time')
    def validate_time(cls, v):
        if v is not None:
            if len(v.strip()) == 0:
                raise ValueError('Time cannot be empty')
            return v.strip()
        return v

# ======= DASHBOARD =======
@router.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ======= LIST VIDEOS =======
@router.get("/videos")
async def list_videos(request: Request):
    try:
        video_collection = get_video_collection()
        if video_collection is None:
            return templates.TemplateResponse(
                "list_videos.html",
                {"request": request, "videos": [], "error": "Database connection unavailable"}
            )
        
        videos = await video_collection.find().to_list(100)
        return templates.TemplateResponse(
            "list_videos.html",
            {"request": request, "videos": videos}
        )
    except PyMongoError as e:
        logger.error(f"Database error in list_videos: {e}")
        return templates.TemplateResponse(
            "list_videos.html",
            {"request": request, "videos": [], "error": "Failed to load videos"}
        )
    except Exception as e:
        logger.error(f"Unexpected error in list_videos: {e}")
        return templates.TemplateResponse(
            "list_videos.html",
            {"request": request, "videos": [], "error": "An unexpected error occurred"}
        )


# ======= ADD VIDEO =======
@router.get("/videos/add")
async def add_video_form(request: Request):
    return templates.TemplateResponse("add_video.html", {"request": request})


@router.post("/videos/add")
async def add_video(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    time: str = Form(...),
    url: str = Form(...),
):
    try:
        # Validate input data
        video_data = VideoCreate(
            title=title,
            description=description,
            time=time,
            url=url
        )
        
        video_collection = get_video_collection()
        if video_collection is None:
            return templates.TemplateResponse(
                "add_video.html",
                {
                    "request": request,
                    "error": "Database connection unavailable",
                    "title": title,
                    "description": description,
                    "time": time,
                    "url": url
                }
            )
        
        # Create new video document
        new_video = {
            "title": video_data.title,
            "description": video_data.description,
            "time": video_data.time,
            "url": str(video_data.url),
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        
        result = await video_collection.insert_one(new_video)
        if result.inserted_id:
            logger.info(f"Video added successfully with ID: {result.inserted_id}")
            return RedirectResponse(url="/videos", status_code=303)
        else:
            raise Exception("Failed to insert video")
            
    except ValueError as e:
        logger.warning(f"Validation error in add_video: {e}")
        return templates.TemplateResponse(
            "add_video.html",
            {
                "request": request,
                "error": str(e),
                "title": title,
                "description": description,
                "time": time,
                "url": url
            }
        )
    except PyMongoError as e:
        logger.error(f"Database error in add_video: {e}")
        return templates.TemplateResponse(
            "add_video.html",
            {
                "request": request,
                "error": "Failed to save video to database",
                "title": title,
                "description": description,
                "time": time,
                "url": url
            }
        )
    except Exception as e:
        logger.error(f"Unexpected error in add_video: {e}")
        return templates.TemplateResponse(
            "add_video.html",
            {
                "request": request,
                "error": "An unexpected error occurred",
                "title": title,
                "description": description,
                "time": time,
                "url": url
            }
        )


# ======= UPDATE VIDEO =======
@router.get("/videos/update")
async def update_video_form(request: Request):
    return templates.TemplateResponse("update_video.html", {"request": request})


@router.post("/videos/update")
async def update_video(
    request: Request,
    id: str = Form(...),
    title: str = Form(None),
    description: str = Form(None),
    time: str = Form(None),
    url: str = Form(None),
):
    try:
        # Validate ObjectId
        try:
            video_id = ObjectId(id)
        except InvalidId:
            return templates.TemplateResponse(
                "update_video.html",
                {
                    "request": request,
                    "error": "Invalid video ID format",
                    "id": id,
                    "title": title,
                    "description": description,
                    "time": time,
                    "url": url
                }
            )
        
        video_collection = get_video_collection()
        if video_collection is None:
            return templates.TemplateResponse(
                "update_video.html",
                {
                    "request": request,
                    "error": "Database connection unavailable",
                    "id": id,
                    "title": title,
                    "description": description,
                    "time": time,
                    "url": url
                }
            )
        
        # Check if video exists
        existing_video = await video_collection.find_one({"_id": video_id})
        if not existing_video:
            return templates.TemplateResponse(
                "update_video.html",
                {
                    "request": request,
                    "error": "Video not found",
                    "id": id,
                    "title": title,
                    "description": description,
                    "time": time,
                    "url": url
                }
            )
        
        # Prepare update data
        update_fields = {}
        if title and title.strip():
            update_fields["title"] = title.strip()
        if description and description.strip():
            update_fields["description"] = description.strip()
        if time and time.strip():
            update_fields["time"] = time.strip()
        if url and url.strip():
            update_fields["url"] = url.strip()
        
        if not update_fields:
            return templates.TemplateResponse(
                "update_video.html",
                {
                    "request": request,
                    "error": "No fields to update",
                    "id": id,
                    "title": title,
                    "description": description,
                    "time": time,
                    "url": url
                }
            )
        
        # Validate update data
        try:
            video_update = VideoUpdate(**update_fields)
        except ValueError as e:
            return templates.TemplateResponse(
                "update_video.html",
                {
                    "request": request,
                    "error": str(e),
                    "id": id,
                    "title": title,
                    "description": description,
                    "time": time,
                    "url": url
                }
            )
        
        # Update video
        update_data = {k: v for k, v in video_update.dict().items() if v is not None}
        if update_data:
            update_data["updated_at"] = datetime.utcnow()
            result = await video_collection.update_one(
                {"_id": video_id},
                {"$set": update_data}
            )
            
            if result.modified_count > 0:
                logger.info(f"Video updated successfully: {video_id}")
                return RedirectResponse(url="/videos", status_code=303)
            else:
                return templates.TemplateResponse(
                    "update_video.html",
                    {
                        "request": request,
                        "error": "No changes were made",
                        "id": id,
                        "title": title,
                        "description": description,
                        "time": time,
                        "url": url
                    }
                )
        
        return RedirectResponse(url="/videos", status_code=303)
        
    except PyMongoError as e:
        logger.error(f"Database error in update_video: {e}")
        return templates.TemplateResponse(
            "update_video.html",
            {
                "request": request,
                "error": "Failed to update video in database",
                "id": id,
                "title": title,
                "description": description,
                "time": time,
                "url": url
            }
        )
    except Exception as e:
        logger.error(f"Unexpected error in update_video: {e}")
        return templates.TemplateResponse(
            "update_video.html",
            {
                "request": request,
                "error": "An unexpected error occurred",
                "id": id,
                "title": title,
                "description": description,
                "time": time,
                "url": url
            }
        )


# ======= DELETE VIDEO =======
@router.get("/videos/delete")
async def delete_video_form(request: Request):
    return templates.TemplateResponse("delete_video.html", {"request": request})


@router.post("/videos/delete")
async def delete_video(request: Request, id: str = Form(...)):
    try:
        # Validate ObjectId
        try:
            video_id = ObjectId(id)
        except InvalidId:
            return templates.TemplateResponse(
                "delete_video.html",
                {
                    "request": request,
                    "error": "Invalid video ID format",
                    "id": id
                }
            )
        
        video_collection = get_video_collection()
        if video_collection is None:
            return templates.TemplateResponse(
                "delete_video.html",
                {
                    "request": request,
                    "error": "Database connection unavailable",
                    "id": id
                }
            )
        
        # Check if video exists before deleting
        existing_video = await video_collection.find_one({"_id": video_id})
        if not existing_video:
            return templates.TemplateResponse(
                "delete_video.html",
                {
                    "request": request,
                    "error": "Video not found",
                    "id": id
                }
            )
        
        # Delete video
        result = await video_collection.delete_one({"_id": video_id})
        
        if result.deleted_count > 0:
            logger.info(f"Video deleted successfully: {video_id}")
            return RedirectResponse(url="/videos", status_code=303)
        else:
            return templates.TemplateResponse(
                "delete_video.html",
                {
                    "request": request,
                    "error": "Failed to delete video",
                    "id": id
                }
            )
            
    except PyMongoError as e:
        logger.error(f"Database error in delete_video: {e}")
        return templates.TemplateResponse(
            "delete_video.html",
            {
                "request": request,
                "error": "Failed to delete video from database",
                "id": id
            }
        )
    except Exception as e:
        logger.error(f"Unexpected error in delete_video: {e}")
        return templates.TemplateResponse(
            "delete_video.html",
            {
                "request": request,
                "error": "An unexpected error occurred",
                "id": id
            }
        )
