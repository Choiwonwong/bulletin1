from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="resources/templates")

api_router_view = APIRouter(
    tags=["post"],
)


@api_router_view.get("/", response_class=HTMLResponse, tags=["main"])
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="main.html")


@api_router_view.get("/posts", response_class=HTMLResponse, tags=["post"])
async def get_post_list_view(request: Request):
    return templates.TemplateResponse(request=request, name="main.html")


@api_router_view.get("/auth", response_class=HTMLResponse, tags=["auth"])
async def get_post_list_view(request: Request):
    return templates.TemplateResponse(request=request, name="auth.html")
