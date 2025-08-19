from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path
import datetime
from typing import List, Dict

app = FastAPI(title="Downloads Organizer")

# Allow frontend to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5174"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def scan_downloads() -> List[Dict]:
    """Scan Downloads folder and return file info"""
    downloads_path = Path.home() / "Downloads"
    files = []
    
    for file_path in downloads_path.iterdir():
        if file_path.is_file():
            try:
                stat = file_path.stat()
                files.append({
                    "name": file_path.name,
                    "size_mb": round(stat.st_size / (1024 * 1024), 2),
                    "extension": file_path.suffix.lower(),
                    "age_days": (datetime.datetime.now() - 
                               datetime.datetime.fromtimestamp(stat.st_birthtime)).days,
                    "created": datetime.datetime.fromtimestamp(stat.st_birthtime).isoformat()
                })
            except Exception as e:
                print(f"Error scanning {file_path}: {e}")
    
    return files

@app.get("/")
async def root():
    return {"message": "Downloads Organizer API is running! 🚀"}

@app.get("/api/files")
async def get_files():
    files = scan_downloads()
    return {
        "files": files,
        "total_count": len(files),
        "message": f"Found {len(files)} files in Downloads"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)