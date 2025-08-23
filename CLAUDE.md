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
python run.py  # Runs on http://localhost:8000

# Linting and code quality
pylint app/  # Run linter on app directory only (ignores venv/)

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
├── main.tsx                   # React app entry point with black background layout
├── components/
│   ├── file-info-card.tsx     # File listing card with API integration
│   ├── anthropic-info-card.tsx # Deletion suggestions card
│   ├── delete-button.tsx      # Red dangerous action button
│   ├── trash-button.tsx       # Yellow-orange caution button
│   └── ui/                    # Radix UI + shadcn/ui components
├── services/api/
│   └── api.ts                # Backend API client with fetchFiles and fetchCandidates
├── types/
│   └── api.ts                # TypeScript interfaces for API responses
└── lib/
    └── utils.ts              # Utility functions (tailwind-merge, clsx)
```

### API Endpoints
- `GET /`: Health check ("Downloads Organizer API is running!")
- `GET /api/files`: Returns file metadata with schema containing files array, total_count, and message
- `GET /api/files/suggestions/cleanup`: Uses Anthropic API to suggest files safe for deletion
- `POST /api/files/suggestions/cleanup/trash`: Moves suggested files to trash
- `POST /api/files/move`: Moves specified files to target folder
- `POST /api/files/move_all`: Moves all files to target folder
- `DELETE /api/files/suggestions/cleanup/delete`: Permanently deletes files from trash
- Interactive API docs available at `http://localhost:8000/docs`

### Key Components
- **File Scanner**: Extracts metadata including name, size_mb, extension, age_days, and created timestamp
- **Anthropic Integration**: Uses Claude API to intelligently suggest files safe for deletion (requires ANTHROPIC_API_KEY)
- **Component Architecture**: Standalone card components with motion animations and loading states
- **UI System**: Built on Radix UI primitives with Tailwind CSS v4 and shadcn/ui components
- **CORS Configuration**: Supports both `http://localhost:3000` and `http://localhost:5174` (Vite default)
- **Error Handling**: Comprehensive error handling for file access and API issues
- **Settings Management**: Environment-based configuration with `.env` file support

## Development Notes

- Backend uses app factory pattern with modular router structure
- File names must use underscores (not hyphens) for Python import compatibility
- Frontend uses Vite's default port (5174) for development
- The application scans the user's Downloads folder using `Path.home() / "Downloads"`
- Virtual environment is pre-configured in `backend/venv/`
- Frontend components use Motion/Framer Motion for animations and hover effects
- API responses are cached globally (DELETION_CANDIDATES) for trash operations
- Environment variable `VITE_API_BASE_URL` can override default backend URL
- Component styling follows glassmorphism design with backdrop-blur effects

## Code Quality and Linting

- Backend follows strict linting standards with pylint (module docstrings, function docstrings, proper imports)
- Frontend uses ESLint with TypeScript for code quality
- Import order: standard library imports before third-party imports
- ES modules used throughout frontend (requires `__dirname` workarounds in config files)
- All functions require proper type annotations and docstrings
- Global variables use UPPER_CASE naming convention