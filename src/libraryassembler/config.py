"""Application configuration utilities."""
from __future__ import annotations

from dataclasses import dataclass, field
import os
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from flask import Flask


_DEF_DB_FILENAME = "libraryassembler.db"


def _default_database_url() -> str:
    """Build the default database URL for a local SQLite database."""
    base_dir = Path(os.getenv("LIBRARYASSEMBLER_HOME", Path.cwd()))
    db_path = base_dir / _DEF_DB_FILENAME
    return f"sqlite:///{db_path}"


def _bool_from_env(value: str | None, *, default: bool = False) -> bool:
    """Parse a boolean environment variable."""
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y", "on"}


@dataclass(slots=True)
class AppConfig:
    """Configuration container with sane defaults for the application."""

    app_name: str = "LibraryAssembler"
    secret_key: str = field(default_factory=lambda: os.getenv("SECRET_KEY", "change-me"))
    database_url: str = field(default_factory=lambda: os.getenv("DATABASE_URL", _default_database_url()))
    sql_echo: bool = field(default_factory=lambda: _bool_from_env(os.getenv("SQLALCHEMY_ECHO")))
    environment: str = field(default_factory=lambda: os.getenv("FLASK_ENV", os.getenv("ENVIRONMENT", "development")))
    testing: bool = field(default_factory=lambda: _bool_from_env(os.getenv("TESTING")))

    @classmethod
    def from_env(cls) -> "AppConfig":
        """Build a configuration object using environment variables."""
        return cls()

    def apply(self, app: "Flask") -> None:
        """Apply the configuration to a Flask application instance."""
        app.config.update(
            APP_NAME=self.app_name,
            SECRET_KEY=self.secret_key,
            SQLALCHEMY_DATABASE_URI=self.database_url,
            SQLALCHEMY_ECHO=self.sql_echo,
            ENV=self.environment,
            TESTING=self.testing,
        )


__all__ = ["AppConfig"]
