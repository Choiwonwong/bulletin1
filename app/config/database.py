from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from app.entity.user import User  # noqa
from app.entity.post import Post  # noqa

engine = None


def init_db(
    database_url: str,
    pool_size: int = 5,
    max_overflow: int = 10,
    pool_timeout: int = 30,
    pool_recycle: int = 3600,
    echo: bool = True,
):
    global engine
    engine = create_engine(
        database_url,
        pool_size=pool_size,
        max_overflow=max_overflow,
        pool_timeout=pool_timeout,
        pool_recycle=pool_recycle,
        echo=echo,
    )


def create_db_and_tables():
    if engine is None:
        raise RuntimeError("Database engine not initialized. Call init_db() first.")
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    if engine is None:
        raise RuntimeError("Database engine not initialized. Call init_db() first.")
    with Session(engine) as session:
        yield session
