"""Ingestion-related models."""
from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from sqlalchemy import DateTime, Enum as SQLEnum, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class IngestionStatus(str, Enum):
    """Lifecycle states for an ingestion job."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


class IngestionJob(Base):
    """Tracks the ingestion of library items from external sources."""

    __tablename__ = "ingestion_jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str] = mapped_column(String(128), nullable=False)
    status: Mapped[IngestionStatus] = mapped_column(
        SQLEnum(IngestionStatus, name="ingestion_status"), nullable=False, default=IngestionStatus.PENDING
    )
    payload: Mapped[Optional[str]] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
    error_message: Mapped[Optional[str]] = mapped_column(Text())

    def mark_failed(self, message: str) -> None:
        """Mark the job as failed with an explanatory message."""
        self.status = IngestionStatus.FAILED
        self.error_message = message

    def mark_completed(self) -> None:
        """Mark the job as completed."""
        self.status = IngestionStatus.COMPLETED
        self.error_message = None

    def __repr__(self) -> str:  # pragma: no cover - debugging helper
        return f"<IngestionJob id={self.id!r} status={self.status!r}>"


__all__ = ["IngestionJob", "IngestionStatus"]
