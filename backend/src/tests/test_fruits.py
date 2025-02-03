import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.fruits.models import DBFruit

from . import assertions


@pytest.fixture(autouse=True, scope="function")
def fake_fruits_db(db_session: Session) -> None:
    try:
        db_session.add_all(
            (
                DBFruit(name="Apple", color="Red"),
                DBFruit(name="Banana", color="Yellow"),
            )
        )
        db_session.commit()
    finally:
        db_session.close()


def test_get_fruits(client: TestClient) -> None:
    response = client.get("/fruits")
    assertions.assert_status_code(response, expected=200)
    assertions.assert_response_json(
        response,
        expected=[
            {"id": 1, "name": "Apple", "color": "Red"},
            {"id": 2, "name": "Banana", "color": "Yellow"},
        ],
    )


def test_get_fruit(client: TestClient) -> None:
    response = client.get("/fruits/2")
    assertions.assert_status_code(response, expected=200)
    assertions.assert_response_json(response, expected={"id": 2, "name": "Banana", "color": "Yellow"})


def test_get_non_existing_fruit(client: TestClient) -> None:
    response = client.get("/fruits/3")
    assertions.assert_status_code(response, expected=404)
    assertions.assert_response_json(response, expected={"detail": "Fruit with id 3 not found"})


def test_add_fruit(client: TestClient) -> None:
    response = client.post("/fruits", json={"name": "orange", "color": "orange"})
    assertions.assert_status_code(response, expected=201)
    assertions.assert_response_json(response, expected={"id": 3, "name": "Orange", "color": "Orange"})

    response = client.get("/fruits")
    assertions.assert_status_code(response, expected=200)
    assertions.assert_response_json(
        response,
        expected=[
            {"id": 1, "name": "Apple", "color": "Red"},
            {"id": 2, "name": "Banana", "color": "Yellow"},
            {"id": 3, "name": "Orange", "color": "Orange"},
        ],
    )


def test_edit_fruit(client: TestClient) -> None:
    response = client.put("/fruits/1", json={"color": "green"})
    assertions.assert_status_code(response, expected=200)
    assertions.assert_response_json(response, expected={"id": 1, "name": "Apple", "color": "Green"})

    response = client.get("/fruits")
    assertions.assert_status_code(response, expected=200)
    assertions.assert_response_json(
        response,
        expected=[
            {"id": 1, "name": "Apple", "color": "Green"},
            {"id": 2, "name": "Banana", "color": "Yellow"},
        ],
    )


def test_edit_non_existing_fruit(client: TestClient) -> None:
    response = client.put("/fruits/3", json={"color": "green"})
    assertions.assert_status_code(response, expected=404)
    assertions.assert_response_json(response, expected={"detail": "Fruit with id 3 not found"})


def test_delete_fruit(client: TestClient) -> None:
    response = client.delete("/fruits/2")
    assertions.assert_status_code(response, expected=204)
    assertions.assert_empty_response(response)

    response = client.get("/fruits")
    assertions.assert_status_code(response, expected=200)
    assertions.assert_response_json(
        response,
        expected=[
            {"id": 1, "name": "Apple", "color": "Red"},
        ],
    )


def test_delete_non_existing_fruit(client: TestClient) -> None:
    response = client.delete("/fruits/3")
    assertions.assert_status_code(response, expected=404)
    assertions.assert_response_json(response, expected={"detail": "Fruit with id 3 not found"})
