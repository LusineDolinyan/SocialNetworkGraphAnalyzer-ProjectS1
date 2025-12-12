from .user import User

class SocialGraph:
    def __init__(self):
        self.users = {}

    def add_user(self, name: str):
        if name in self.users:
            raise ValueError(f"User {name} already exists.")
        self.users[name] = User(name)

    def remove_user(self, name: str):
        if name not in self.users:
            raise ValueError(f"User {name} not found.")

        # remove from all friends' lists
        for friend in list(self.users[name].friends.keys()):
            self.users[friend].remove_friend(name)

        del self.users[name]

    def add_friend(self, name1: str, name2: str, weight: int = 1, comment: str = ""):
        if name1 not in self.users or name2 not in self.users:
            raise ValueError("One of the users was not found.")

        self.users[name1].add_friend(name2, weight, comment)
        self.users[name2].add_friend(name1, weight, comment)

    def remove_friend(self, name1: str, name2: str):
        if name1 not in self.users or name2 not in self.users:
            raise ValueError("One of the users was not found.")

        self.users[name1].remove_friend(name2)
        self.users[name2].remove_friend(name1)

    def get_friends(self, name: str):
        if name not in self.users:
            raise ValueError("User not found.")
        return list(self.users[name].friends.items())  # list of (friend_name, weight)

    def __repr__(self):
        return f"SocialGraph({list(self.users.keys())})"
