class User:
    def __init__(self, name: str):
        self.name = name
        self.friends = set()

    def add_friend(self, other_name: str):
        self.friends.add(other_name)

    def remove_friend(self, other_name: str):
        self.friends.discard(other_name)

    def __repr__(self):
        return f"User({self.name})"

"What this code does:"

"Stores the username"

"Stores friends as a set"

"Allows you to add and remove friends"

"Pretty output of the user to the console"

