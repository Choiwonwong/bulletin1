from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import BIGINT, TEXT, Column, Identity
from sqlalchemy.orm import Mapped
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User


class Post(SQLModel, table=True):
    __tablename__ = "posts"

    id: Mapped[UUID] = Field(
        default_factory=uuid4, primary_key=True, index=True, nullable=False
    )
    post_number: Mapped[int] = Field(
        default=None,
        sa_column=Column(
            "post_number",
            BIGINT,
            Identity(start=1),
            unique=True,
            nullable=False,
            index=True,
        ),
    )

    title: Mapped[str] = Field(index=True, max_length=200)
    content: Mapped[str] = Field(sa_column=Column(TEXT))
    view_count: Mapped[int] = Field(default=0, nullable=False)

    created_at: Mapped[datetime] = Field(
        default_factory=datetime.now(UTC), nullable=False
    )
    modified_at: Mapped[datetime | None] = Field(
        default=None, sa_column_kwargs={"onupdate": datetime.now(UTC)}
    )

    deleted: Mapped[bool] = Field(default=False, nullable=False)
    deleted_at: Mapped[datetime | None] = Field(default=None)

    user_id: Mapped[UUID] = Field(foreign_key="users.id", index=True)

    author: Mapped[User] = Relationship(back_populates="posts")
