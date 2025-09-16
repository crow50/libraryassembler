"""Homepage routes for LibraryAssembler."""
from __future__ import annotations

from flask import Blueprint, current_app, jsonify

bp = Blueprint("home", __name__)


@bp.get("/")
def index():
    """Return a friendly JSON message for the homepage."""
    app_config = current_app.config.get("APP_CONFIG")
    app_name = getattr(app_config, "app_name", current_app.config.get("APP_NAME", "LibraryAssembler"))
    return jsonify({
        "app": app_name,
        "message": "Welcome to the LibraryAssembler service.",
    })
