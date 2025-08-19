# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Downloads Organizer is a full-stack web application that scans and analyzes files in the Downloads folder. The project consists of a FastAPI backend with a modular architecture and a React frontend built with TypeScript and Vite.

## Technology Stack

- **Backend**: FastAPI (Python) with uvicorn server, pydantic-settings for configuration
- **Frontend**: React 19 with TypeScript, Vite for build tooling
- **Environment**: Python 3.11 with virtual environment

## Development Commands

### Backend Development
```bash
# Setup
cd backend
source venv/bin/activate
pip install -r requirements.txt

# Run development server with hot reload
python run.py  # Runs on http://0.0.0.0:8000

# Install new dependencies
pip install <package_name>
pip freeze > requirements.txt
```

### Frontend Development
```bash
# Setup
cd frontend
npm install

# Development server
npm run dev        # Runs on http://localhost:5174
npm run build      # Build for production
npm run preview    # Preview production build
npm run lint       # Run ESLint
```

## Project Architecture

### Backend Structure (`backend/app/`)
```
app/
├── main.py                    # FastAPI app factory with CORS configuration
├── config.py                  # Settings management with pydantic-settings
├── api/routers/
│   ├── files.py              # Files API endpoints
│   └── health.py             # Health check endpoint
├── models/
│   └── files.py              # Pydantic response models
└── operations/
    └── file_operations.py    # Business logic for file scanning
```

### Frontend Structure (`frontend/src/`)
```
src/
├── main.tsx                   # React app entry point
├── components/
│   └── downloads-list.tsx     # Main file display component
├── services/api/
│   └── api.ts                # Backend API client
└── types/
    └── api.ts                # TypeScript interfaces
```

### API Endpoints
- `GET /`: Health check ("Downloads Organizer API is running!")
- `GET /api/files`: Returns file metadata with schema containing files array, total_count, and message
- Interactive API docs available at `http://localhost:8000/docs`

### Key Components
- **File Scanner**: Extracts metadata including name, size_mb, extension, age_days, and created timestamp
- **CORS Configuration**: Supports both `http://localhost:3000` and `http://localhost:5174` (Vite default)
- **Error Handling**: Comprehensive error handling for file access issues
- **Settings Management**: Environment-based configuration with `.env` file support

## Development Notes

- Backend uses app factory pattern with modular router structure
- File names must use underscores (not hyphens) for Python import compatibility
- Frontend uses Vite's default port (5174) for development
- The application scans the user's Downloads folder using `Path.home() / "Downloads"`
- Virtual environment is pre-configured in `backend/venv/`