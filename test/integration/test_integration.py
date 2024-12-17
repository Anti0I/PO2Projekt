from app.app import app
from pytest import fixture
from flask.testing import FlaskClient
import json


@fixture
def client() -> FlaskClient:
    return app.test_client()


def reset_file():
    with open("./app/users.json", "w") as f:
        json.dump([], f)


def setup_test_user():
    with open("./app/users.json", "w") as f:
        json.dump([{"id": 1, "name": "Antoni", "lastname": "Kmuk"}], f)


def test_get_all_users(client: FlaskClient):
    setup_test_user()
    response = client.get("/users")
    assert response.status_code == 200


def test_get_user_by_id(client: FlaskClient):
    setup_test_user()
    response = client.get("/users/1")
    assert response.status_code == 200


def test_get_user_wrong_id(client: FlaskClient):
    setup_test_user()
    response = client.get("/users/999")
    assert response.status_code == 400


def test_patch_user(client: FlaskClient):
    setup_test_user()
    response = client.patch("/users/1", json={"name": "Antoni"})
    assert response.status_code == 204


def test_patch_wrong_user(client: FlaskClient):
    setup_test_user()
    response = client.patch("/users/999", json={"name": "Antoni"})
    assert response.status_code == 400


def test_put_user(client: FlaskClient):
    setup_test_user()
    response = client.put("/users/1", json={"name": "Antoni", "lastname": "Kmuk"})
    assert response.status_code == 204


def test_delete_user(client: FlaskClient):
    setup_test_user()
    response = client.delete("/users/1")
    assert response.status_code == 204


def test_delete_wrong_user(client: FlaskClient):
    setup_test_user()
    response = client.delete("/users/999")
    assert response.status_code == 400


def test_post_user(client: FlaskClient):
    reset_file()
    response = client.post("/users", json={"name": "Antoni", "lastname": "Kmuk"})
    assert response.status_code == 201
