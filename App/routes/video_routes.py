from fastapi import APIRouter

router = APIRouter(prefix="/videos", tags=["Videos"])

@router.get("/")
async def list_videos():
    return {"message": "Here we will list videos from MongoDB"}
