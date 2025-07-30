from abc import ABC, abstractmethod

from dto.create_post import CreatePost
from dto.post_response import PostResponse
from dto.update_post import UpdatePost


class PostService(ABC):
    @abstractmethod
    def get_posts(self, sort: str | None) -> list[PostResponse]:
        pass

    @abstractmethod
    def get_post(self, post_number: int) -> PostResponse:
        pass

    @abstractmethod
    def create_post(self, create_post: CreatePost) -> int:
        pass

    @abstractmethod
    def update_post(self, update_post: UpdatePost) -> PostResponse:
        pass

    @abstractmethod
    def delete_post(self, post_number: int) -> int:
        pass
