class User:
    def __init__(self, name: str):
        self.name = name

        # friends → { friend_name: weight }
        self.friends = {}

        # comments → { friend_name: "text" }
        self.comments = {}

    def add_friend(self, friend_name: str, weight: int = 1, comment: str = ""):
        if friend_name in self.friends:
            raise ValueError(f"{friend_name} is already a friend of {self.name}.")
        self.friends[friend_name] = weight
        self.comments[friend_name] = comment

    def remove_friend(self, friend_name: str):
        if friend_name not in self.friends:
            raise ValueError(f"{friend_name} is not a friend of {self.name}.")
        del self.friends[friend_name]
        if friend_name in self.comments:
            del self.comments[friend_name]

    def update_weight(self, friend_name: str, weight: int):
        if friend_name not in self.friends:
            raise ValueError(f"{friend_name} is not a friend.")
        self.friends[friend_name] = weight

    def add_comment(self, friend_name: str, comment: str):
        if friend_name not in self.friends:
            raise ValueError(f"{friend_name} is not a friend.")
        self.comments[friend_name] = comment

    def __repr__(self):
        return f"User({self.name})"
