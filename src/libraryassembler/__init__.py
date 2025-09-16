"""LibraryAssembler Flask application factory."""
from __future__ import annotations

import click
from flask import Flask

from .config import AppConfig
from .database import init_app as init_database, init_db
from .routes import register_blueprints


def create_app(config: AppConfig | None = None) -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    config = config or AppConfig.from_env()
    config.apply(app)
    app.config["APP_CONFIG"] = config

    init_database(app)
    register_blueprints(app)

    @app.cli.command("init-db")
    def init_db_command() -> None:
        """Initialise the SQL database tables."""
        init_db()
        click.echo("Database initialised.")

    return app


__all__ = ["create_app", "AppConfig"]
