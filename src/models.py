"""SQLAlchemy models for the early LibraryAssembler prototype."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from libraryassembler.database import Base


class User(Base):
    """Represents an application user."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    library_items: Mapped[list[LibraryItem]] = relationship(
        "LibraryItem", back_populates="owner", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<User id={self.id!r} email={self.email!r}>"


class LibraryItem(Base):
    """Represents a single item managed by the library."""

    __tablename__ = "library_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    media_type: Mapped[str] = mapped_column(String(50), nullable=False)
    file_path: Mapped[str] = mapped_column(String(1024), nullable=False)
    isbn: Mapped[str | None] = mapped_column(String(32))
    cover_url: Mapped[str | None] = mapped_column(String(1024))
    description: Mapped[str | None] = mapped_column(String(2000))
    published_date: Mapped[str | None] = mapped_column(String(50))
    publisher: Mapped[str | None] = mapped_column(String(255))
    added_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped[User] = relationship("User", back_populates="library_items")

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<LibraryItem id={self.id!r} title={self.title!r}>"


__all__ = ["Base", "User", "LibraryItem"]
