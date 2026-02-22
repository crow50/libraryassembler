"""Flask routes for early LibraryAssembler API scaffolding."""
from __future__ import annotations

from flask import Blueprint, jsonify

api = Blueprint("api", __name__, url_prefix="/api")


@api.get("/health")
def health_check():
    return jsonify({"status": "ok", "message": "LibraryAssembler API is healthy"})


@api.get("/library")
def list_library_items():
    # Placeholder data until ingestion is wired in.
    return jsonify(
        {
            "items": [
                {
                    "id": 1,
                    "title": "Example Library Item",
                    "media_type": "ebook",
                    "status": "placeholder",
                }
            ]
        }
    )


__all__ = ["api"]
