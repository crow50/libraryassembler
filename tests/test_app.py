from __future__ import annotations

from pathlib import Path

from sqlalchemy import select

from libraryassembler import AppConfig, create_app
from libraryassembler.database import init_db, session_scope
from libraryassembler.models import Book


def build_test_config(tmp_path: Path) -> AppConfig:
    db_path = tmp_path / "test.db"
    return AppConfig(
        database_url=f"sqlite:///{db_path}",
        testing=True,
        sql_echo=False,
        secret_key="test-secret",
    )


def test_healthcheck_endpoint(tmp_path):
    app = create_app(build_test_config(tmp_path))
    with app.app_context():
        init_db()

    client = app.test_client()
    response = client.get("/api/health")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["status"] == "ok"
    assert payload["media_items"] == 0
    assert payload["ingestion_jobs"] == 0


def test_homepage_returns_welcome_message(tmp_path):
    app = create_app(build_test_config(tmp_path))
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["app"] == "LibraryAssembler"
    assert "welcome" in payload["message"].lower()


def test_init_db_cli(tmp_path):
    app = create_app(build_test_config(tmp_path))
    runner = app.test_cli_runner()
    result = runner.invoke(args=["init-db"])
    assert result.exit_code == 0
    assert "Database initialised." in result.output


def test_book_model_can_insert_and_query(tmp_path):
    app = create_app(build_test_config(tmp_path))
    db_path = tmp_path / "test.db"

    with app.app_context():
        init_db()
        assert db_path.exists()

        with session_scope() as session:
            session.add(Book(title="Example", author="Author", file_path="/books/example.epub"))

        with session_scope() as session:
            retrieved = session.execute(select(Book).where(Book.title == "Example")).scalar_one()
            assert retrieved.author == "Author"
            assert retrieved.file_path == "/books/example.epub"
