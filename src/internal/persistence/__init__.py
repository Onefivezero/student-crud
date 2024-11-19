from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


engine = create_engine('sqlite+pysqlite:///:memory:?check_same_thread=False', poolclass=StaticPool)


def create_session():
    session = sessionmaker(bind=engine, expire_on_commit=False)
    return session()
