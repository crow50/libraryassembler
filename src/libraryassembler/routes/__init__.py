"""Route registration helpers."""
from __future__ import annotations

from flask import Flask

from .health import bp as health_bp
from .home import bp as home_bp


def register_blueprints(app: Flask) -> None:
    """Attach all application blueprints to the Flask instance."""
    app.register_blueprint(home_bp)
    app.register_blueprint(health_bp)


__all__ = ["register_blueprints"]
