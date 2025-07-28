import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import create_db_and_tables, init_db
from .settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info(
        f"Initializing database connection for: {settings.db_type} at {settings.database_url}"
    )
    db_settings = settings.current_db_settings
    init_db(
        settings.database_url,
        pool_size=db_settings.pool_size,
        max_overflow=db_settings.max_overflow,
        pool_timeout=db_settings.pool_timeout,
        pool_recycle=db_settings.pool_recycle,
        echo=True,
    )

    if settings.app_env == "local":
        logging.info("Running create_db_and_tables() for local environment...")
        create_db_and_tables()
        logging.info("Database tables created/checked for local environment.")
    else:
        logging.info(
            f"Skipping create_db_and_tables() for {settings.app_env} environment."
        )

    yield
    logging.info("Application shutting down. Performing cleanup...")
