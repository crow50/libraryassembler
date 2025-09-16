"""Database utilities built around SQLAlchemy."""
from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

from flask import Flask, g
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""


_engine: Engine | None = None
_session_factory: sessionmaker[Session] | None = None


def init_engine(database_url: str, *, echo: bool = False) -> Engine:
    """Initialise the global SQLAlchemy engine."""
    global _engine
    _engine = create_engine(database_url, echo=echo, future=True)
    return _engine


def get_engine() -> Engine:
    """Return the configured SQLAlchemy engine."""
    if _engine is None:
        raise RuntimeError("The SQLAlchemy engine has not been initialised.")
    return _engine


def init_session_factory(engine: Engine | None = None) -> sessionmaker[Session]:
    """Create a session factory tied to the provided engine."""
    global _session_factory
    engine = engine or get_engine()
    _session_factory = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    return _session_factory


def get_session_factory() -> sessionmaker[Session]:
    """Return the configured session factory."""
    if _session_factory is None:
        raise RuntimeError("The SQLAlchemy session factory has not been initialised.")
    return _session_factory


@contextmanager
def session_scope() -> Iterator[Session]:
    """Provide a transactional scope around a series of operations."""
    factory = get_session_factory()
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

    app.extensions["sqlalchemy_engine"] = engine
    app.extensions["sqlalchemy_session_factory"] = factory


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
