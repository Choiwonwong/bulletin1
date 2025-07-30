from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from .config.lifespan import lifespan
from .controller.api.post_controller import post_api_router
from .controller.view.view_controller import api_router_view
from .controller.view.view_test_controller import api_router_view_test

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="resources/static"), name="static")
app.mount("/styles", StaticFiles(directory="resources/styles"), name="styles")

app.include_router(
    post_api_router,
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
