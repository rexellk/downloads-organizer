from pathlib import Path
import datetime
from typing import List, Dict, Union
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

def move_file_operation(file_names, target_folder: str) -> Dict[str, Union[str, List[str]]]:
    """Pure business logic - move file(s) to a target folder"""
    downloads_path = Path.home() / "Downloads"
    target_path = Path(target_folder).expanduser()
    
    if not target_path.exists():
        return {"status": "error", "message": f"Target folder {target_folder} does not exist."}
    
    # Handle both single file and list of files
    if isinstance(file_names, str):
        file_names = [file_names]
    
    moved_files = []
    failed_files = []
    
    for file_name in file_names:
        file_path = downloads_path / file_name
        if not file_path.exists() or not file_path.is_file():
            failed_files.append(f"{file_name}: does not exist")
            continue
        
        try:
            new_location = target_path / file_name
            file_path.rename(new_location)
            moved_files.append(file_name)
        except Exception as e:
            failed_files.append(f"{file_name}: {str(e)}")
    
    if not moved_files and failed_files:
        return {"status": "error", "message": f"Failed to move files: {', '.join(failed_files)}"}
    elif moved_files and failed_files:
        return {
            "status": "partial", 
            "message": f"Moved {len(moved_files)} files, {len(failed_files)} failed",
            "moved": moved_files,
            "failed": failed_files
        }
    else:
        return {
            "status": "success", 
            "message": f"Moved {len(moved_files)} file(s) to {target_folder}",
            "moved": moved_files
        }

def move_all_files_operation(target_folder: str) -> Dict[str, Union[str, List[str]]]:
    """Pure business logic - move all files to a target folder"""
    downloads_path = Path.home() / "Downloads"
    target_path = Path(target_folder).expanduser()
    
    if not target_path.exists():
        return {"status": "error", "message": f"Target folder {target_folder} does not exist."}
    
    moved_files = []
    for file_path in downloads_path.iterdir():
        if file_path.is_file():
            try:
                new_location = target_path / file_path.name
                file_path.rename(new_location)
                moved_files.append(file_path.name)
            except Exception as e:
                print(f"Error moving {file_path}: {e}")
    
    return {"status": "success", "message": f"Moved {len(moved_files)} files to {target_folder}.", "files": moved_files}