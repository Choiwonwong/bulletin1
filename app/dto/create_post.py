from uuid import UUID

from pydantic import BaseModel


class CreatePost(BaseModel):
    title: str
    content: str
    user_id: UUID
