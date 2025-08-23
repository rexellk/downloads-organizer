"""Pydantic models for file-related API responses."""
from typing import List

from pydantic import BaseModel


class FileInfo(BaseModel):
    """Model representing file metadata information."""
    name: str
    size_mb: float
    extension: str
    age_days: int
    created: str


class FilesResponse(BaseModel):
    """Model for API response containing multiple files."""
    files: List[FileInfo]
    total_count: int
    message: str