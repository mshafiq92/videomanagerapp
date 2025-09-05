from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.dbConnection import video_collection
from bson.objectid import ObjectId

templates = Jinja2Templates(directory="templates")
router = APIRouter()

# ======= LIST VIDEOS =======
@router.get("/videos")
async def list_videos(request: Request):
    videos = list(video_collection.find())
    return templates.TemplateResponse("list.html", {"request": request, "videos": videos})


# ======= ADD VIDEO =======
@router.get("/videos/add")
async def add_video_form(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})

@router.post("/videos/add")
async def add_video(title: str = Form(...), url: str = Form(...), description: str = Form("")):
    video_collection.insert_one({"title": title, "url": url, "description": description})
    return RedirectResponse(url="/videos", status_code=303)


# ======= UPDATE VIDEO =======
@router.get("/videos/update/{video_id}")
async def update_video_form(request: Request, video_id: str):
    video = video_collection.find_one({"_id": ObjectId(video_id)})
    return templates.TemplateResponse("update.html", {"request": request, "video": video})

@router.post("/videos/update/{video_id}")
async def update_video(video_id: str, title: str = Form(...), url: str = Form(...), description: str = Form("")):
    video_collection.update_one(
        {"_id": ObjectId(video_id)},
        {"$set": {"title": title, "url": url, "description": description}}
    )
    return RedirectResponse(url="/videos", status_code=303)


# ======= DELETE VIDEO =======
@router.get("/videos/delete/{video_id}")
async def delete_video(video_id: str):
    video_collection.delete_one({"_id": ObjectId(video_id)})
    return RedirectResponse(url="/videos", status_code=303)
