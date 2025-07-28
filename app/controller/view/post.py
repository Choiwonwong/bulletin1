from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="resources/templates")

api_router_post_view = APIRouter(
    tags=["post"],
)


@api_router_post_view.get("/", response_class=HTMLResponse, tags=["view", "main"])
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="main.html")


@api_router_post_view.get("/posts", response_class=HTMLResponse)
async def get_post_list_view(request: Request):
    return templates.TemplateResponse(request=request, name="post_list.html")


@api_router_post_view.get("/posts/{post_id}", response_class=HTMLResponse)
async def get_post_detail_view(request: Request, post_id: str):
    return templates.TemplateResponse(
        request=request, name="post_list.html", context={"post_id": post_id}
    )
