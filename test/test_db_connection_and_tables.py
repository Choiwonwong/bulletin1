import logging

import pytest
from sqlmodel import SQLModel, create_engine

from app.config.settings import settings

# Configure logger for this test module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set to INFO or DEBUG for more verbose output


@pytest.fixture(scope="module")
def db_engine():
    # Store original host to restore later
    original_host = settings.mysql.host

    # Temporarily override host for testing
    settings.mysql.host = "127.0.0.1"
    logger.info(f"Overriding MySQL host for test to: {settings.mysql.host}")

    db_url = settings.database_url
    logger.info(f"Attempting to connect to: {db_url}")

    engine = create_engine(
        db_url, echo=True, pool_pre_ping=True, connect_args={"unix_socket": None}
    )

    try:
        # Ensure connection is established and metadata reflected once for the module
        with engine.connect() as connection:
            logger.info("Successfully connected to the database in fixture.")
            SQLModel.metadata.reflect(bind=engine)
            logger.info("Database metadata reflected in fixture.")
        yield engine  # Yield the engine for tests to use
    except Exception as e:
        logger.error(f"Failed to set up database engine in fixture: {e}")
        pytest.fail(f"Failed to set up database engine for tests: {e}")
    finally:
        engine.dispose()
        logger.info("Database engine disposed in fixture teardown.")
        # Restore original host
        settings.mysql.host = original_host
        logger.info(f"Restored MySQL host to: {settings.mysql.host}")


def test_db_connection(db_engine):
    """Test if the database connection can be established."""
    try:
        with db_engine.connect() as connection:
            logger.info("Test: Successfully established database connection.")
            assert connection is not None
    except Exception as e:
        pytest.fail(f"Test: Failed to establish database connection: {e}")


def test_users_table_exists(db_engine):
    """Test if the 'users' table exists in the database."""
    # Metadata is already reflected in the fixture, so we can directly check
    logger.info("Test: Checking for 'users' table existence.")
    assert "users" in SQLModel.metadata.tables, (
        "Table 'users' does not exist in the database."
    )
    logger.info("Test: Table 'users' found.")


def test_posts_table_exists(db_engine):
    """Test if the 'posts' table exists in the database."""
    # Metadata is already reflected in the fixture, so we can directly check
    logger.info("Test: Checking for 'posts' table existence.")
    assert "posts" in SQLModel.metadata.tables, (
        "Table 'posts' does not exist in the database."
    )
    logger.info("Test: Table 'posts' found.")
