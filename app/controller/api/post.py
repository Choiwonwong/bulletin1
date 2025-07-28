from fastapi import APIRouter

api_router_post = APIRouter(
    prefix="/posts",
    tags=["post"],
)

@api_router_post.get("/")
async def get_posts():
    return [{"id": 1, "title": "test"}, {"id": 2, "title": "test2"}]

@api_router_post.get("/{post_id}")
async def get_post(post_id: str):
    return {"id": post_id, "title": "test"}


