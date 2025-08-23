"""File operations for scanning, moving, and deleting files."""
import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union

from app.models.files import FileInfo, FilesResponse


def scan_downloads_operation() -> FilesResponse:
    """Scan Downloads folder and return file information."""
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
                    "age_days": (
                        datetime.datetime.now() -
                        datetime.datetime.fromtimestamp(stat.st_birthtime)
                    ).days,
                    "created": datetime.datetime.fromtimestamp(
                        stat.st_birthtime
                    ).isoformat()
                })
            except (OSError, ValueError) as error:
                print(f"Error scanning {file_path}: {error}")

    files = [FileInfo(**file_data) for file_data in files_data]
    return FilesResponse(
        files=files,
        total_count=len(files),
        message=f"Found {len(files)} files in Downloads"
    )


def move_file_operation(
    file_names: Union[str, List[str]], 
    target_folder: str
) -> Dict[str, Union[str, List[str]]]:
    """Move file(s) to a target folder."""
    downloads_path = Path.home() / "Downloads"
    target_path = Path(target_folder).expanduser()

    if not target_path.exists():
        return {
            "status": "error", 
            "message": f"Target folder {target_folder} does not exist."
        }

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
        except (OSError, PermissionError) as error:
            failed_files.append(f"{file_name}: {str(error)}")

    if not moved_files and failed_files:
        return {
            "status": "error", 
            "message": f"Failed to move files: {', '.join(failed_files)}"
        }

    if moved_files and failed_files:
        return {
            "status": "partial",
            "message": f"Moved {len(moved_files)} files, {len(failed_files)} failed",
            "moved": moved_files,
            "failed": failed_files
        }

    return {
        "status": "success",
        "message": f"Moved {len(moved_files)} file(s) to {target_folder}",
        "moved": moved_files
    }


def move_all_files_operation(target_folder: str) -> Dict[str, Union[str, List[str]]]:
    """Move all files to a target folder."""
    downloads_path = Path.home() / "Downloads"
    target_path = Path(target_folder).expanduser()

    if not target_path.exists():
        return {
            "status": "error", 
            "message": f"Target folder {target_folder} does not exist."
        }

    moved_files = []
    for file_path in downloads_path.iterdir():
        if file_path.is_file():
            try:
                new_location = target_path / file_path.name
                file_path.rename(new_location)
                moved_files.append(file_path.name)
            except (OSError, PermissionError) as error:
                print(f"Error moving {file_path}: {error}")

    return {
        "status": "success", 
        "message": f"Moved {len(moved_files)} files to {target_folder}.",
        "files": moved_files
    }


def delete_files_bin(file_names: Optional[List[str]] = None) -> Dict[str, Union[str, List[str]]]:
    """Permanently delete files from trash bin."""
    bin_path = Path.home() / ".Trash"
    deleted_files = []

    if not bin_path.exists():
        return {"status": "error", "message": "Trash folder not found"}

    try:
        files_to_delete = (
            list(bin_path.iterdir()) if file_names is None 
            else [bin_path / name for name in file_names]
        )
    except PermissionError:
        return {
            "status": "error", 
            "message": "Permission denied: Cannot access trash folder"
        }

    for file_path in files_to_delete:
        if file_path.is_file() and file_path.exists():
            try:
                file_path.unlink()
                deleted_files.append(file_path.name)
            except PermissionError:
                print(f"Permission denied deleting {file_path}")
            except OSError as error:
                print(f"Error deleting {file_path}: {error}")

    return {
        "status": "success", 
        "message": f"Permanently deleted {len(deleted_files)} files",
        "files": deleted_files
    }