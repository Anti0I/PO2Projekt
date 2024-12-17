import json
from flask.typing import ResponseReturnValue


class User_controller:
    @staticmethod
    def get_user(user_id: int = None) -> ResponseReturnValue:
        with open("./app/users.json", "r") as f:
            users = json.load(f)

        if user_id is not None:
            for user in users:
                if user["id"] == user_id:
                    return user
            return "", 400
        return users

    @staticmethod
    def add_user(user: dict) -> ResponseReturnValue:
        with open("./app/users.json", "r") as f:
            users = json.load(f)

        user_id = 1 if not users else max(u["id"] for u in users) + 1

        user["id"] = user_id
        users.append(user)
        users.sort(key=lambda u: u["id"])

        with open("./app/users.json", "w") as f:
            json.dump(users, f)

        return user, 201

    @staticmethod
    def update_user(user_id: int, user: dict) -> ResponseReturnValue:
        with open("./app/users.json", "r") as f:
            users = json.load(f)

        for u in users:
            if u["id"] == user_id:
                u.update(user)
                with open("./app/users.json", "w") as f:
                    json.dump(users, f)
                return "", 204
        return "", 400

    @staticmethod
    def put_user(user_id: int, user: dict) -> ResponseReturnValue:
        with open("./app/users.json", "r") as f:
            users = json.load(f)

        for i, u in enumerate(users):
            if u["id"] == user_id:
                user["id"] = user_id
                users[i] = user
                with open("./app/users.json", "w") as f:
                    json.dump(users, f)
                return "", 204

        user["id"] = user_id
        users.append(user)
        with open("./app/users.json", "w") as f:
            json.dump(users, f)
        return "", 204

    @staticmethod
    def delete_user(user_id: int) -> ResponseReturnValue:
        with open("./app/users.json", "r") as f:
            users = json.load(f)

        for i, u in enumerate(users):
            if u["id"] == user_id:
                users.pop(i)
                with open("./app/users.json", "w") as f:
                    json.dump(users, f)
                return "", 204
        return "", 400
