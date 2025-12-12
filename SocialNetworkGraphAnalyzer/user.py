class User:
    def __init__(self, name: str):
        self.name = name  # User's name

        # Dictionary to store friends and their connection weights
        # key: friend's name, value: weight (int)
        self.friends = {}

        # Dictionary to store comments about friends
        # key: friend's name, value: comment text
        self.comments = {}

    def add_friend(self, friend_name: str, weight: int = 1, comment: str = ""):
        # Add a new friend with optional weight and comment
        if friend_name in self.friends:
            raise ValueError(f"{friend_name} is already a friend of {self.name}.")
        self.friends[friend_name] = weight  # Set friendship weight
        self.comments[friend_name] = comment  # Store comment

    def remove_friend(self, friend_name: str):
        # Remove a friend and their comment
        if friend_name not in self.friends:
            raise ValueError(f"{friend_name} is not a friend of {self.name}.")
        del self.friends[friend_name]  # Remove from friends
        if friend_name in self.comments:
            del self.comments[friend_name]  # Remove associated comment

    def update_weight(self, friend_name: str, weight: int):
        # Update the weight of an existing friendship
        if friend_name not in self.friends:
            raise ValueError(f"{friend_name} is not a friend.")
        self.friends[friend_name] = weight

    def add_comment(self, friend_name: str, comment: str):
        # Update or add a comment for a friend
        if friend_name not in self.friends:
            raise ValueError(f"{friend_name} is not a friend.")
        self.comments[friend_name] = comment

    def __repr__(self):
        # String representation showing the user's name
        return f"User({self.name})"
