"""Database utilities built around SQLAlchemy."""
from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Iterator

from flask import Flask, current_app, g, has_app_context
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""


_EXTENSION_KEY = "libraryassembler_database"


def init_engine(database_url: str, *, echo: bool = False) -> Engine:
    """Initialise a SQLAlchemy engine for the provided database URL."""
    return create_engine(database_url, echo=echo, future=True)


def _get_state(app: Flask | None = None) -> dict[str, Any]:
    """Return the database state stored on the Flask application."""

    if app is None:
        if not has_app_context():
            raise RuntimeError(
                "Database access requires an application context. Call ``create_app`` "
                "and use ``app.app_context()`` or pass an explicit ``app`` argument."
            )
        app = current_app._get_current_object()

    state = app.extensions.get(_EXTENSION_KEY)
    if state is None:
        raise RuntimeError("The SQLAlchemy engine has not been initialised for this Flask application.")
    return state


def get_engine(app: Flask | None = None) -> Engine:
    """Return the configured SQLAlchemy engine."""

    return _get_state(app)["engine"]


def init_session_factory(engine: Engine | None = None, *, app: Flask | None = None) -> sessionmaker[Session]:
    """Create a session factory tied to the provided engine."""

    if engine is None:
        engine = get_engine(app)
    return sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_session_factory(app: Flask | None = None) -> sessionmaker[Session]:
    """Return the configured session factory."""

    return _get_state(app)["session_factory"]


@contextmanager
def session_scope(app: Flask | None = None) -> Iterator[Session]:
    """Provide a transactional scope around a series of operations."""
    factory = get_session_factory(app)
    session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init_app(app: Flask) -> None:
    """Configure the Flask app with database helpers."""
    engine = init_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=app.config.get("SQLALCHEMY_ECHO", False))
    factory = init_session_factory(engine)

    app.extensions[_EXTENSION_KEY] = {"engine": engine, "session_factory": factory}

    # Retain backwards compatibility with previous extension keys, if any callers expect them.
    app.extensions["sqlalchemy_engine"] = engine
    app.extensions["sqlalchemy_session_factory"] = factory

    @app.teardown_appcontext
    def cleanup_session(exception: BaseException | None = None) -> None:
        session: Session | None = g.pop("db_session", None)
        if session is None:
            return
        if exception is not None:
            session.rollback()
        else:
            try:
                session.commit()
            except Exception:  # pragma: no cover - defensive cleanup
                session.rollback()
                raise
        session.close()


def get_session() -> Session:
    """Return a request-scoped session, creating one if necessary."""
    if "db_session" not in g:
        factory = get_session_factory()
        g.db_session = factory()
    return g.db_session


def init_db() -> None:
    """Create all database tables registered on the declarative base."""
    # Import models so they are registered with the metadata before creation.
    from . import models  # noqa: F401  # pylint: disable=unused-import

    engine = get_engine()
    Base.metadata.create_all(bind=engine)


__all__ = [
    "Base",
    "get_engine",
    "get_session",
    "init_app",
    "init_db",
    "init_engine",
    "init_session_factory",
    "session_scope",
]
