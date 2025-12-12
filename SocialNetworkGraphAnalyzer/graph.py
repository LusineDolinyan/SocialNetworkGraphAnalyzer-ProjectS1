from .user import User

class SocialGraph:
    def __init__(self):
        # Dictionary to store all users; key: username, value: User object
        self.users = {}

    def add_user(self, name: str):
        # Add a new user to the graph
        if name in self.users:
            raise ValueError(f"User {name} already exists.")
        self.users[name] = User(name)  # Create User object

    def remove_user(self, name: str):
        # Remove a user and all references from friends
        if name not in self.users:
            raise ValueError(f"User {name} not found.")

        # Remove this user from all their friends' lists
        for friend in list(self.users[name].friends.keys()):
            self.users[friend].remove_friend(name)

        # Delete the user from the graph
        del self.users[name]

    def add_friend(self, name1: str, name2: str, weight: int = 1, comment: str = ""):
        # Add a friendship (bidirectional) with optional weight and comment
        if name1 not in self.users or name2 not in self.users:
            raise ValueError("One of the users was not found.")

        self.users[name1].add_friend(name2, weight, comment)
        self.users[name2].add_friend(name1, weight, comment)

    def remove_friend(self, name1: str, name2: str):
        # Remove friendship between two users (bidirectional)
        if name1 not in self.users or name2 not in self.users:
            raise ValueError("One of the users was not found.")

        self.users[name1].remove_friend(name2)
        self.users[name2].remove_friend(name1)

    def get_friends(self, name: str):
        # Return list of friends with their weights and comments
        if name not in self.users:
            raise ValueError("User not found.")
        return list(self.users[name].friends.items())

    def __repr__(self):
        # String representation showing all usernames
        return f"SocialGraph({list(self.users.keys())})"
