from flask import Flask, request, jsonify
from flask.typing import ResponseReturnValue
from app.controller import User_controller

app = Flask(__name__)


@app.get("/users")
def users():
    controller = User_controller()
    return controller.get_user()


@app.get("/users/<int:user_id>")
def user(user_id: int):
    controller = User_controller()
    return controller.get_user(user_id)


@app.post("/users")
def add_user():
    controller = User_controller()
    user = request.json
    return controller.add_user(user)


@app.patch("/users/<int:user_id>")
def update_user(user_id: int):
    controller = User_controller()
    user = request.json
    return controller.update_user(user_id, user)


@app.put("/users/<int:user_id>")
def put_user(user_id: int):
    controller = User_controller()
    user = request.json
    return controller.put_user(user_id, user)


@app.delete("/users/<int:user_id>")
def delete_user(user_id: int):
    controller = User_controller()
    return controller.delete_user(user_id)


if __name__ == "__main__":
    app.run()
