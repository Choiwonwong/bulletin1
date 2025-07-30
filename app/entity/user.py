from datetime import UTC, datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .post import Post


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(
        default_factory=uuid4, primary_key=True, index=True, nullable=False
    )

    nickname: str = Field(max_length=50)
    email: str = Field(unique=True, index=True, max_length=100)
    password: str

    created_at: datetime = Field(default_factory=datetime.now(UTC), nullable=False)
    modified_at: datetime | None = Field(
        default=None, sa_column_kwargs={"onupdate": datetime.now(UTC)}
    )

    deleted: bool = Field(default=False, nullable=False)
    deleted_at: datetime | None = Field(default=None)

    posts: Optional[list["Post"]] = Relationship(back_populates="author")  # 1:N
