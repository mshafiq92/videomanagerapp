from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId
from app.dbConnection import video_collection

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# ======= DASHBOARD =======
@router.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ======= LIST VIDEOS =======
@router.get("/videos")
async def list_videos(request: Request):
    videos = await video_collection.find().to_list(100)
    return templates.TemplateResponse(
        "list_videos.html", {"request": request, "videos": videos}
    )


# ======= ADD VIDEO =======
@router.get("/add")
async def add_video_form(request: Request):
    return templates.TemplateResponse("add_video.html", {"request": request})


@router.post("/add")
async def add_video(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    time: str = Form(...),
    url: str = Form(...),
):
    new_video = {
        "title": title,
        "description": description,
        "time": time,
        "url": url,
    }
    await video_collection.insert_one(new_video)
    return RedirectResponse(url="/videos", status_code=303)


# ======= UPDATE VIDEO =======
@router.get("/update")
async def update_video_form(request: Request):
    return templates.TemplateResponse("update_video.html", {"request": request})


@router.post("/update")
async def update_video(
    request: Request,
    id: str = Form(...),
    title: str = Form(None),
    description: str = Form(None),
    time: str = Form(None),
    url: str = Form(None),
):
    update_data = {}
    if title:
        update_data["title"] = title
    if description:
        update_data["description"] = description
    if time:
        update_data["time"] = time
    if url:
        update_data["url"] = url

    if update_data:
        await video_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": update_data}
        )

    return RedirectResponse(url="/videos", status_code=303)


# ======= DELETE VIDEO =======
@router.get("/delete")
async def delete_video_form(request: Request):
    return templates.TemplateResponse("delete_video.html", {"request": request})


@router.post("/delete")
async def delete_video(request: Request, id: str = Form(...)):
    await video_collection.delete_one({"_id": ObjectId(id)})
    return RedirectResponse(url="/videos", status_code=303)
