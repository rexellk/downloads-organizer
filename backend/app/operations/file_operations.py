from pathlib import Path
import datetime
from typing import List, Dict
from app.models.files import FileInfo, FilesResponse

def scan_downloads_operation() -> FilesResponse:
    """Pure business logic - scan Downloads folder and return file info"""
    downloads_path = Path.home() / "Downloads"
    files_data = []
    
    for file_path in downloads_path.iterdir():
        if file_path.is_file():
            try:
                stat = file_path.stat()
                files_data.append({
                    "name": file_path.name,
                    "size_mb": round(stat.st_size / (1024 * 1024), 2),
                    "extension": file_path.suffix.lower(),
                    "age_days": (datetime.datetime.now() - 
                               datetime.datetime.fromtimestamp(stat.st_birthtime)).days,
                    "created": datetime.datetime.fromtimestamp(stat.st_birthtime).isoformat()
                })
            except Exception as e:
                print(f"Error scanning {file_path}: {e}")
    
    files = [FileInfo(**file_data) for file_data in files_data]
    return FilesResponse(
        files=files,
        total_count=len(files),
        message=f"Found {len(files)} files in Downloads"
    )