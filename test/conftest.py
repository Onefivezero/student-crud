import os
import pytest
from sqlalchemy import create_engine, NullPool
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient
from testcontainers.postgres import PostgresContainer

from src.app.app import app
from src.internal.model.base import Base
from src.internal.persistence import get_db


@pytest.fixture(scope="session", autouse=True)
def postgres_container():
    with PostgresContainer("postgres:16-alpine") as postgres:
        url = postgres.get_connection_url()
        print(f"DEBUG: Container started at {url}")

        os.environ["DATABASE_URL"] = url
        yield postgres


@pytest.fixture(scope="session", autouse=True)
def test_engine(postgres_container):
    engine = create_engine(
        os.environ["DATABASE_URL"],
    )

    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session(test_engine):
    connection = test_engine.connect()
    transaction = connection.begin()
    session_local = sessionmaker(bind=connection, expire_on_commit=False)
    session = session_local()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def client(db_session):
    app.dependency_overrides[get_db] = lambda: db_session

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()