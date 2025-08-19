# Downloads Organizer Backend

A FastAPI-based backend service for scanning and analyzing files in the Downloads folder.

## Architecture Overview

The backend follows a modular FastAPI architecture with clear separation of concerns:

```
backend/
├── app/                       # Main application package
│   ├── main.py               # FastAPI app factory and configuration
│   ├── config.py             # Application settings and environment configuration
│   ├── api/                  # API layer
│   │   └── routers/          # API route handlers
│   │       ├── files.py      # File-related endpoints
│   │       └── health.py     # Health check endpoints
│   ├── models/               # Data models
│   │   └── files.py          # Pydantic response models for file data
│   └── operations/           # Business logic layer
│       └── file_operations.py # Core file scanning and processing logic
├── requirements.txt          # Python dependencies
├── run.py                   # Development server entry point
└── venv/                    # Python virtual environment
```

## Folder Structure Details

### `/app`
Main application package containing all source code.

### `/app/main.py`
- FastAPI application factory
- CORS configuration for frontend integration
- Router registration and middleware setup

### `/app/config.py`
- Application settings using pydantic-settings
- Environment variable management
- Configuration for development and production environments

### `/app/api/routers/`
API endpoint definitions organized by domain:
- `files.py`: File scanning and metadata retrieval endpoints
- `health.py`: System health and status endpoints

### `/app/models/`
Pydantic models for request/response validation:
- `files.py`: Data models for file metadata and API responses

### `/app/operations/`
Business logic and core functionality:
- `file_operations.py`: File system operations, scanning logic, and metadata extraction

## Development Setup

1. **Environment Setup**:
   ```bash
   cd backend
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run Development Server**:
   ```bash
   python run.py
   ```
   Server runs on `http://0.0.0.0:8000`

3. **API Documentation**:
   Interactive docs available at `http://localhost:8000/docs`

## API Endpoints

- `GET /`: Health check endpoint
- `GET /api/files`: Returns file metadata from Downloads folder

## Technology Stack

- **Framework**: FastAPI with uvicorn server
- **Configuration**: pydantic-settings for environment management
- **Python Version**: 3.11+
- **Key Features**: 
  - Automatic file scanning
  - Metadata extraction (name, size, extension, age)
  - CORS support for frontend integration
  - Comprehensive error handling