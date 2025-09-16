"""WSGI entrypoint for running the application with ``flask --app``."""
from __future__ import annotations

from . import create_app

app = create_app()

__all__ = ["app"]
