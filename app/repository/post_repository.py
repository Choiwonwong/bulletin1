from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from app.dto.create_post import CreatePost
from app.dto.delete_post import DeletePost
from app.dto.update_post import UpdatePost

if TYPE_CHECKING:
    from app.entity.post import Post


class PostRepository(ABC):
    @abstractmethod
    def get_all(self, sort: str | None) -> list[Post]:
        pass

    @abstractmethod
    def get(self, post_number: int) -> Post | None:
        pass

    @abstractmethod
    def save(self, create_post: CreatePost) -> int:
        pass

    @abstractmethod
    def update(self, update_post: UpdatePost) -> int | None:
        pass

    @abstractmethod
    def delete(self, delete_post: DeletePost) -> int | None:
        pass
