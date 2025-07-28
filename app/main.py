from fastapi import FastAPI
from starlette.templating import Jinja2Templates

from .config.lifespan import lifespan
from .controller.api.post import api_router_post
from .controller.view.post import api_router_post_view

app = FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory="resources/templates")

app.include_router(
    api_router_post,
    prefix="/api",
    tags=["api"],
)

app.include_router(
    api_router_post_view,
    tags=["view"],
)
