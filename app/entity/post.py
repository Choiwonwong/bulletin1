from datetime import UTC, datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import BIGINT, TEXT, Column, Identity
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from entity.user import User


class Post(SQLModel, table=True):
    __tablename__ = "posts"

    id: UUID = Field(
        default_factory=uuid4, primary_key=True, index=True, nullable=False
    )
    post_number: int = Field(
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

    title: str = Field(index=True, min_length=1, max_length=200)
    content: str = Field(sa_column=Column(TEXT))
    view_count: int = Field(default=0, nullable=False)

    created_at: datetime = Field(default_factory=datetime.now(UTC), nullable=False)
    modified_at: datetime | None = Field(
        default=None, sa_column_kwargs={"onupdate": datetime.now(UTC)}
    )

    deleted: bool = Field(default=False, nullable=False)
    deleted_at: datetime | None = Field(default=None)

    user_id: UUID = Field(foreign_key="users.id", index=True)

    author: "User" = Relationship(back_populates="posts")
