"""Media item model definition."""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class MediaItem(Base):
    """Represents an item in the managed digital library."""

    __tablename__ = "media_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[Optional[str]] = mapped_column(String(255))
    media_type: Mapped[Optional[str]] = mapped_column(String(64))
    source: Mapped[Optional[str]] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def __repr__(self) -> str:  # pragma: no cover - debugging helper
        return f"<MediaItem id={self.id!r} title={self.title!r}>"


__all__ = ["MediaItem"]
