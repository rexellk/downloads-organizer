# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Downloads Organizer is a web-based tool that scans and analyzes files in the Downloads folder. The project consists of a FastAPI backend that provides file scanning capabilities and API endpoints.

## Technology Stack

- **Backend**: FastAPI (Python) with uvicorn server
- **Environment**: Python 3.11 with virtual environment

## Development Commands

### Backend Setup
```bash
cd backend
source venv/bin/activate  # Activate virtual environment
pip install -r requirements.txt  # Install dependencies
```

### Running the Backend
```bash
cd backend
source venv/bin/activate
python main.py  # Runs on http://0.0.0.0:8000
```

### Installing Dependencies
```bash
cd backend
source venv/bin/activate
pip install <package_name>
pip freeze > requirements.txt  # Update requirements
```

## Project Architecture

### Backend Structure (`backend/`)
- `main.py`: FastAPI application with file scanning functionality
- `requirements.txt`: Python dependencies
- `venv/`: Python virtual environment

### Key Components
- **File Scanner**: Scans Downloads folder and extracts file metadata (size, extension, age, creation date)
- **API Endpoints**:
  - `GET /`: Health check endpoint
  - `GET /api/files`: Returns scanned file information with metadata
- **CORS**: Configured for frontend at `http://localhost:3000`

### File Analysis Features
The backend analyzes downloaded files and provides:
- File name and extension
- File size in MB
- File age in days
- Creation timestamp
- Total file count

## Development Notes

- The virtual environment is already set up in `backend/venv/`
- FastAPI automatically generates interactive API docs at `/docs` when running
- The application scans the user's Downloads folder using `Path.home() / "Downloads"`
- Error handling is implemented for file access issues