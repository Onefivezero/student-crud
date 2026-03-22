import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_engine():
    database_url = os.getenv("DATABASE_URL", "sqlite:///:memory:")

    connect_args = {}
    if database_url.startswith("sqlite"):
        connect_args["check_same_thread"] = False

    return create_engine(database_url, connect_args=connect_args)

def get_db():
    engine = get_engine()
    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()