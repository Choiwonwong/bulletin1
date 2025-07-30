from uuid import UUID

from pydantic import BaseModel


class UpdatePost(BaseModel):
    title: str | None
    content: str | None
    user_id: UUID
