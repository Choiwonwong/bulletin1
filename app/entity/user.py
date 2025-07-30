from datetime import UTC, datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .post import Post


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Mapped[UUID] = Field(
        default_factory=uuid4, primary_key=True, index=True, nullable=False
    )

    nickname: Mapped[str | None] = Field(max_length=50)
    email: Mapped[str] = Field(unique=True, index=True, max_length=100)
    password: Mapped[str]

    created_at: Mapped[datetime] = Field(
        default_factory=datetime.now(UTC), nullable=False
    )
    modified_at: Mapped[datetime | None] = Field(
        default=None, sa_column_kwargs={"onupdate": datetime.now(UTC)}
    )

    deleted: Mapped[bool] = Field(default=False, nullable=False)
    deleted_at: Mapped[datetime | None] = Field(default=None)

    posts: Mapped[list["Post"]] = Relationship(back_populates="author")  # 1:N
