"""Book model representing managed ebooks."""
from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class Book(Base):
    """Represents a single book available in the library."""

    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(1024), nullable=False)

    def __repr__(self) -> str:  # pragma: no cover - debugging helper
        return f"<Book id={self.id!r} title={self.title!r}>"


__all__ = ["Book"]
