from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from entity.post import Post


class PostResponse(BaseModel):
    id: int
    post_number: int
    title: str
    content: str
    view_count: int
    created_at: datetime
    modified_at: datetime
    author: str

    @classmethod
    def with_post(cls, post: Post):
        return cls(
            id=post.id,
            post_number=post.post_number,
            title=post.title,
            content=post.content,
            view_count=post.view_count,
            created_at=post.created_at,
            modified_at=post.modified_at,
            author=post.author,
        )
