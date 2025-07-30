from dto.create_post import CreatePost
from dto.delete_post import DeletePost
from dto.post_response import PostResponse
from dto.update_post import UpdatePost
from fastapi import APIRouter
from service.post_service import PostService
from service.post_service_impl import PostServiceImpl

post_api_router = APIRouter(
    prefix="/posts",
    tags=["post"],
)

post_service: PostService = PostServiceImpl()


@post_api_router.get("")
async def get_posts() -> list[PostResponse]:
    return post_service.get_posts(sort=None)


@post_api_router.get("/{post_number}")
async def get_post(post_number: str) -> PostResponse | None:
    return post_service.get_post(post_number)


@post_api_router.post("")
async def create_post(create_post: CreatePost) -> int:
    return post_service.create_post(create_post)


@post_api_router.put("")
async def modified_post(update_post: UpdatePost) -> int | None:
    return post_service.update_post(update_post)


@post_api_router.delete("/{post_number}")
async def delete_post(delete_post: DeletePost) -> int | None:
    return post_service.delete_post(delete_post)
