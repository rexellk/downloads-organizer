"""API router for file operations endpoints."""
from typing import List, Union

from fastapi import APIRouter

from app.models.files import FilesResponse
from app.operations.anthropic_sort import prompt_deletion_candidates
from app.operations.file_operations import (
    delete_files_bin,
    move_all_files_operation,
    move_file_operation,
    scan_downloads_operation,
)

# Global variable to store deletion candidates between requests
DELETION_CANDIDATES = None

router = APIRouter(prefix="/api", tags=["files"])


@router.get("/files", response_model=FilesResponse)
async def get_files():
    """Get all files in the Downloads folder."""
    return scan_downloads_operation()


@router.get("/files/suggestions/cleanup")
async def get_cleanup_suggestions():
    """Get AI-powered suggestions for files that can be deleted."""
    global DELETION_CANDIDATES  # pylint: disable=global-statement
    files_data = scan_downloads_operation()
    file_names = [file.name for file in files_data.files]
    DELETION_CANDIDATES = prompt_deletion_candidates(file_names)
    return DELETION_CANDIDATES


@router.post("/files/suggestions/cleanup/trash")
async def trash_candidates():
    """Move suggested deletion candidates to trash."""
    if DELETION_CANDIDATES is None or not DELETION_CANDIDATES:
        return "Please get AI Suggestions First before trashing"
    return move_file_operation(DELETION_CANDIDATES, "~/.Trash")


@router.post("/files/move")
async def move_file(file_names: Union[str, List[str]], target_folder: str):
    """Move specified files to target folder."""
    return move_file_operation(file_names, target_folder)


@router.post("/files/move_all")
async def move_all_files(target_folder: str):
    """Move all files to target folder."""
    return move_all_files_operation(target_folder)


@router.delete("/files/suggestions/cleanup/delete")
async def delete_candidates():
    """Permanently delete files from trash."""
    return delete_files_bin()
