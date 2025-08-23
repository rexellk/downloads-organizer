# Backend - Downloads Organizer API

FastAPI backend service for the Downloads Organizer application that provides file scanning, AI-powered deletion suggestions, and file management operations.

## Technology Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Python 3.11** - Programming language
- **Pydantic** - Data validation using Python type annotations
- **Anthropic API** - Claude AI integration for intelligent file suggestions
- **Uvicorn** - ASGI server for running the application

## Quick Start

### Prerequisites
- Python 3.11+
- Virtual environment activated

### Installation & Setup

```bash
# Navigate to backend directory
cd backend

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file for environment variables
# Add your Anthropic API key:
# ANTHROPIC_API_KEY=your_api_key_here

# Run development server
python run.py
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:
- **Interactive API Docs**: `http://localhost:8000/docs` (Swagger UI)
- **Alternative Docs**: `http://localhost:8000/redoc` (ReDoc)

## API Endpoints

### File Operations
- `GET /api/files` - Get all files in Downloads folder with metadata
- `POST /api/files/move` - Move specific files to target folder
- `POST /api/files/move_all` - Move all files to target folder

### AI-Powered Cleanup
- `GET /api/files/suggestions/cleanup` - Get AI suggestions for files safe to delete
- `POST /api/files/suggestions/cleanup/trash` - Move suggested files to trash
- `DELETE /api/files/suggestions/cleanup/delete` - Permanently delete files from trash

### Health Check
- `GET /` - API health status

## Project Structure

```
backend/
├── app/
│   ├── main.py                    # FastAPI app factory and configuration
│   ├── config.py                  # Settings and environment configuration
│   ├── api/routers/
│   │   ├── files.py              # File management endpoints
│   │   └── health.py             # Health check endpoints
│   ├── models/
│   │   └── files.py              # Pydantic data models
│   └── operations/
│       ├── file_operations.py    # File scanning and manipulation logic
│       └── anthropic_sort.py     # AI integration for file suggestions
├── venv/                          # Virtual environment
├── requirements.txt               # Python dependencies
└── run.py                        # Development server launcher
```

## Development

### Code Quality
```bash
# Run linter (from backend directory)
pylint app/

# The codebase follows strict linting standards:
# - All modules, classes, and functions have docstrings
# - Proper import order (standard library before third-party)
# - Type hints for all function parameters and return values
# - Specific exception handling instead of broad Exception catches
```

### Adding New Dependencies
```bash
# Install new package
pip install <package_name>

# Update requirements file
pip freeze > requirements.txt
```

### Environment Variables
Create a `.env` file in the backend directory:
```
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## Features

### File Scanning
- Scans user's Downloads folder (`~/Downloads`)
- Extracts metadata: name, size (MB), extension, age (days), creation date
- Returns structured JSON responses with file information

### AI-Powered Suggestions
- Integrates with Anthropic's Claude API
- Analyzes filenames to suggest safe-to-delete files
- Identifies temporary files, caches, logs, backups, etc.
- Returns JSON array of recommended files for deletion

### File Management
- Move individual or multiple files to specified folders
- Move all files from Downloads to target location
- Trash management (move to system trash)
- Permanent deletion from trash (requires system permissions)

### Error Handling
- Comprehensive error handling for file system operations
- Permission error handling with helpful messages
- API error responses with appropriate HTTP status codes
- Graceful handling of missing files or invalid paths

## Architecture Notes

- **App Factory Pattern**: Clean application initialization and configuration
- **Modular Router Structure**: Organized endpoints by functionality
- **Separation of Concerns**: Business logic separated from API routes
- **Global State Management**: Deletion candidates cached between requests
- **CORS Enabled**: Supports frontend development on multiple ports

## Troubleshooting

### Permission Issues
On macOS, permanent file deletion from trash may require "Full Disk Access" permissions:
1. Open System Settings → Privacy & Security → Full Disk Access
2. Add your Terminal application or Python executable

### Import Errors in IDE
If your IDE shows import errors, ensure it's using the virtual environment:
- VS Code: Set Python interpreter to `backend/venv/bin/python`
- PyCharm: Configure project interpreter to use the virtual environment

### API Connection Issues
- Ensure backend is running on `http://localhost:8000`
- Check CORS settings in `app/config.py` for allowed origins
- Verify frontend is making requests to correct base URL