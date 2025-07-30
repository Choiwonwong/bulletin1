from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="resources/templates")

api_router_view_test = APIRouter()


@api_router_view_test.get("", response_class=HTMLResponse, tags=["main"])
async def root_test(request: Request):
    return templates.TemplateResponse(request=request, name="main_test.html")


@api_router_view_test.get("/posts", response_class=HTMLResponse, tags=["post"])
async def get_post_list_view_test(request: Request):
    return templates.TemplateResponse(request=request, name="main_test.html")
