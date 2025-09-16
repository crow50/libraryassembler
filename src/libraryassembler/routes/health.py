"""Health check endpoints."""
from __future__ import annotations

from flask import Blueprint, jsonify
from sqlalchemy import func, select

from ..database import get_session
from ..models import IngestionJob, MediaItem

bp = Blueprint("health", __name__, url_prefix="/api")


@bp.get("/health")
def healthcheck():
    """Return basic application and database health information."""
    session = get_session()
    media_count = session.scalar(select(func.count(MediaItem.id))) or 0
    ingestion_count = session.scalar(select(func.count(IngestionJob.id))) or 0
    return (
        jsonify(
            {
                "status": "ok",
                "media_items": media_count,
                "ingestion_jobs": ingestion_count,
            }
        ),
        200,
    )


__all__ = ["bp"]
