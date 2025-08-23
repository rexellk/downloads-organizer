from fastapi import APIRouter
from app.operations.file_operations import scan_downloads_operation
from app.operations.file_operations import move_file_operation
from app.operations.file_operations import move_all_files_operation
from app.operations.anthropic_sort import prompt_deletion_candidates
from app.models.files import FilesResponse

deletion_candidates = None

router = APIRouter(prefix="/api", tags=["files"])

@router.get("/files", response_model=FilesResponse)
async def get_files():
    return scan_downloads_operation()

@router.get("/files/suggestions/cleanup")
async def get_cleanup_suggestions():
    global deletion_candidates
    files_data = scan_downloads_operation()
    file_names = [file.name for file in files_data.files]
    deletion_candidates = prompt_deletion_candidates(file_names)
    return deletion_candidates

@router.post("/files/suggestions/cleanup/trash")
async def trash_candidates():
    if (deletion_candidates == ""):
        return "Please get AI Suggestions First before trashing"
    return move_file_operation(deletion_candidates, "~/.Trash")

@router.post("/files/move")
async def move_file(file_names, target_folder: str):
    return move_file_operation(file_names, target_folder)

@router.post("/files/move_all")
async def move_all_files(target_folder: str):
    return move_all_files_operation(target_folder)

