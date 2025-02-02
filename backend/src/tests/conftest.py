from collections.abc import Iterator
from fastapi.testclient import TestClient
from sqlalchemy import Engine, StaticPool, create_engine
from src.main import app
import pytest
from sqlalchemy.orm import sessionmaker, Session
from src.database import Base, get_db


@pytest.fixture(scope="session")
def db_engine() -> Iterator[Engine]:
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    yield engine

    engine.dispose()


@pytest.fixture(scope="session")
def session_local_factory(db_engine: Engine) -> sessionmaker:
    TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    Base.metadata.create_all(bind=db_engine)
    return TestSessionLocal


@pytest.fixture(scope="function", autouse=True)
def db_session(
    db_engine: Engine, session_local_factory: sessionmaker
) -> Iterator[Session]:
    connection = db_engine.connect()
    transaction = connection.begin()

    session = session_local_factory(bind=connection)

    def override_get_db() -> Iterator[Session]:
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield session

    transaction.rollback()
    connection.close()


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)
