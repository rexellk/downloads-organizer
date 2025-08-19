from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/")
async def root():
    return {"message": "Downloads Organizer API is running!"}