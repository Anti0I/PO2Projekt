from pytest import fixture
from app.controller import User_controller
import json


@fixture
def controller() -> User_controller:
    return User_controller()


def reset_file():
    with open("./app/users.json", "w") as f:
        json.dump([], f)


def setup_test_user():
    with open("./app/users.json", "w") as f:
        json.dump([{"id": 1, "name": "Antoni", "lastname": "Kmuk"}], f)


def test_get_all_users(controller: User_controller):
    setup_test_user()
    users = controller.get_user()

    assert users == [{"id": 1, "name": "Antoni", "lastname": "Kmuk"}]


def test_get_user(controller: User_controller):
    setup_test_user()
    user = controller.get_user(1)

    assert user == {"id": 1, "name": "Antoni", "lastname": "Kmuk"}
    reset_file()


def test_get_user_wrong_id(controller: User_controller):
    setup_test_user()
    user = controller.get_user(999)

    assert user == ("", 400)
    reset_file()


def test_add_user(controller: User_controller):
    user = {"name": "Antoni", "lastname": "Kmuk"}
    expected_user = {"id": 1, "name": "Antoni", "lastname": "Kmuk"}

    controller.add_user(user)

    with open("./app/users.json", "r") as f:
        users = json.load(f)

    assert users == [expected_user]
    reset_file()


def test_update_user(controller: User_controller):
    setup_test_user()

    controller.update_user(1, {"lastname": "Kmuk"})

    with open("./app/users.json", "r") as f:
        users = json.load(f)

    assert users[0] == {"id": 1, "name": "Antoni", "lastname": "Kmuk"}
    reset_file()


def test_put_user(controller: User_controller):
    setup_test_user()
    updated_user = {"name": "Antoni", "lastname": "Kmuk"}

    controller.put_user(1, updated_user)

    with open("./app/users.json", "r") as f:
        users = json.load(f)

    assert users[0] == {"id": 1, "name": "Antoni", "lastname": "Kmuk"}
    reset_file()


def test_delete_user(controller: User_controller):
    setup_test_user()

    controller.delete_user(1)

    with open("./app/users.json", "r") as f:
        users = json.load(f)

    assert users == []
    reset_file()
