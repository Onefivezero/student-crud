import unittest

from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from src.app.app import app
from src.internal.model import Base
from src.internal.model.student import Student
from src.internal.persistence import create_session, engine


class TestBase(unittest.TestCase):
    session: Session
    client: TestClient

    @classmethod
    def init_session(cls):
        cls.session = create_session()

    @classmethod
    def close_session(cls):
        cls.session.close()

    @classmethod
    def init_tables(cls):
        Base.metadata.create_all(engine)

    @classmethod
    def cleanup_db(cls):
        Base.metadata.drop_all(engine)

    @classmethod
    def init_client(cls):
        cls.client = TestClient(app)

    def setUp(self):
        self.init_tables()
        self.init_session()
        self.init_client()

    def tearDown(self):
        self.close_session()
        self.cleanup_db()
