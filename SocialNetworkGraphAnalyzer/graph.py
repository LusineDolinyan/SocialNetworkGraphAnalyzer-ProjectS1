from .user import User

class SocialGraph:
    def __init__(self):
        self.users ={}

    def add_user(self, name: str):
        if name in self.users:
            print(f"User {name} already exists.")
            return
        self.users[name] = User(name)

    def remove_user(self, name: str):
        if name not in self.users:
            print(f"User {name} not found.")
            return
        for friend_name in self.users[name].friends:
            self.users[friend_name].remove_friend(name)
        del self.users[name]

    def add_friend(self, name1: str, name2: str):
        if name1 not in self.users or name2 not in self.users:
            raise ValueError("One of the users was not found.")
        self.users[name1].add_friend(name2)
        self.users[name2].add_friend(name1)


    def remove_friend(self, name1: str, name2: str):
        if name1 not in self.users or name2 not in self.users:
            raise ValueError("One of the users was not found.")
        self.users[name1].remove_friend(name2)
        self.users[name2].remove_friend(name1)


    def get_friends(self, name: str):
        if name not in self.users:
            raise ValueError("One of the users was not found.")
        return list(self.users[name].friends)

    def __repr__(self):
        return f"SocialGraph({list(self.users.keys())}"


"Creates a user graph"

"Adds/removes users and friendships"

"Returns a list of friends"

"Prettyly displays the entire network"
