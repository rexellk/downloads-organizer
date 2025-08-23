"""Main FastAPI application factory and configuration."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api.routers import files, health


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    fastapi_app = FastAPI(title=settings.app_name)

    # CORS
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    fastapi_app.include_router(health.router)
    fastapi_app.include_router(files.router)

    return fastapi_app


app = create_app()