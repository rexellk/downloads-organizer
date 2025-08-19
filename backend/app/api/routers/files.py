from fastapi import APIRouter
from app.operations.file_operations import scan_downloads_operation
from app.models.files import FilesResponse

router = APIRouter(prefix="/api", tags=["files"])

@router.get("/files", response_model=FilesResponse)
async def get_files():
    return scan_downloads_operation()