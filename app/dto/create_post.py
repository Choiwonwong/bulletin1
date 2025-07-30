from uuid import UUID

from pydantic import BaseModel, Field


class CreatePost(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    user_id: UUID
