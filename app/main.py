from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from .config.lifespan import lifespan
from .controller.api.post import api_router_post
from .controller.view.view import api_router_view
from .controller.view.view_test import api_router_view_test

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="resources/static"), name="static")
app.mount("/styles", StaticFiles(directory="resources/styles"), name="styles")

app.include_router(
    api_router_post,
    prefix="/api",
    tags=["api"],
)

app.include_router(
    api_router_view,
    tags=["view"],
)

app.include_router(
    api_router_view_test,
    prefix="/test",
    tags=["view", "test"],
)
