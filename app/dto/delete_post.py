from uuid import UUID

from pydantic import BaseModel


class DeletePost(BaseModel):
    post_number: int
    user_id: UUID
