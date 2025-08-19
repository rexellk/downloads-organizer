from pydantic import BaseModel
from typing import List

class FileInfo(BaseModel):
    name: str
    size_mb: float
    extension: str
    age_days: int
    created: str

class FilesResponse(BaseModel):
    files: List[FileInfo]
    total_count: int
    message: str