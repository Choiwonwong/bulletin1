from __future__ import annotations

from typing import TYPE_CHECKING

from dto.create_post import CreatePost
from dto.delete_post import DeletePost
from dto.post_response import PostResponse
from dto.update_post import UpdatePost
from repository.post_repository import PostRepository
from repository.post_repository_impl import PostRepositoryImpl
from service.post_service import PostService

if TYPE_CHECKING:
    from entity.post import Post


class PostServiceImpl(PostService):
    def __init__(self):
        self.post_repository: PostRepository = PostRepositoryImpl()

    def get_posts(self, sort: str | None) -> list[PostResponse]:
        posts: list[Post] = self.post_repository.get_all(sort)
        return [PostResponse.with_post(post) for post in posts]

    def get_post(self, post_number: int) -> PostResponse | None:
        post: Post | None = self.post_repository.get(post_number)
        if post:
            return PostResponse.with_post(post)
        else:
            return None

    def create_post(self, create_post: CreatePost) -> int:
        return self.post_repository.save(create_post=create_post)

    def update_post(self, update_post: UpdatePost) -> int | None:
        update_result: int | None = self.post_repository.update(update_post)
        if update_result:
            return 200
        else:
            return None

    def delete_post(self, delete_post: DeletePost) -> int:
        delete_result: int | None = self.post_repository.delete(delete_post=delete_post)
        if delete_result:
            return 200
        else:
            return None
