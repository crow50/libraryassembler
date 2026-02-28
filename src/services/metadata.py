"""Service for fetching metadata from OpenLibrary."""
from __future__ import annotations

from typing import Any

import requests


class MetadataService:
    """Fetches book metadata from OpenLibrary."""

    BASE_URL = "https://openlibrary.org/isbn/{isbn}.json"
    COVER_URL = "https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"

    def fetch_book_metadata(self, isbn: str) -> dict[str, Any]:
        """Return normalized metadata for a book by ISBN."""
        url = self.BASE_URL.format(isbn=isbn)
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        payload = response.json()

        description = payload.get("description")
        if isinstance(description, dict):
            description = description.get("value")

        cover_url = None
        covers = payload.get("covers")
        if covers:
            cover_url = self.COVER_URL.format(cover_id=covers[0])

        publisher = None
        publishers = payload.get("publishers")
        if publishers:
            publisher = publishers[0]

        return {
            "isbn": isbn,
            "title": payload.get("title"),
            "description": description,
            "published_date": payload.get("publish_date"),
            "publisher": publisher,
            "cover_url": cover_url,
        }
