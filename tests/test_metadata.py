from __future__ import annotations

from unittest.mock import Mock

from services.metadata import MetadataService


def test_fetch_book_metadata_parses_response(monkeypatch):
    isbn = "9780140328721"
    payload = {
        "title": "Matilda",
        "publish_date": "October 1, 1988",
        "publishers": ["Puffin"],
        "covers": [12345],
        "description": {"value": "A story about a brilliant girl."},
    }

    mock_response = Mock()
    mock_response.json.return_value = payload
    mock_response.raise_for_status = Mock()

    def mock_get(url, timeout):
        assert url == f"https://openlibrary.org/isbn/{isbn}.json"
        assert timeout == 10
        return mock_response

    monkeypatch.setattr("services.metadata.requests.get", mock_get)

    service = MetadataService()
    result = service.fetch_book_metadata(isbn)

    assert result == {
        "isbn": isbn,
        "title": "Matilda",
        "description": "A story about a brilliant girl.",
        "published_date": "October 1, 1988",
        "publisher": "Puffin",
        "cover_url": "https://covers.openlibrary.org/b/id/12345-L.jpg",
    }
