from abc import ABC, abstractmethod

from app.dto.create_post import CreatePost
from app.dto.delete_post import DeletePost
from app.dto.post_response import PostResponse
from app.dto.update_post import UpdatePost
from app.repository.post_repository import PostRepository


class PostService(ABC):
    post_repository: PostRepository

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
    def delete_post(self, delete_post: DeletePost) -> int:
        pass
