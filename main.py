from SocialNetworkGraphAnalyzer.graph import SocialGraph
from SocialNetworkGraphAnalyzer.algorithms import (
    common_friends,
    shortest_path,
    recommend_friends,
    recommend_friends_weighted,
    shortest_weighted_path
)

def demo():
    # --------------------------
    # Create social graph & users
    # --------------------------
    g = SocialGraph()
    g.add_user("Kate")
    g.add_user("John")
    g.add_user("Jake")
    g.add_user("Anna")

    # --------------------------
    # Add friendships with weights
    # --------------------------
    g.add_friend("Kate", "Jake", weight=1)
    g.add_friend("Kate", "John", weight=2)
    g.add_friend("Jake", "John", weight=3)

    print("Initial friends:")
    print("Kate:", g.get_friends("Kate"))
    print("John:", g.get_friends("John"))
    print("Jake:", g.get_friends("Jake"))

    # --------------------------
    # Remove a friendship
    # --------------------------
    g.remove_friend("Kate", "John")
    print("\nAfter removing Kate-John friendship:")
    print("Kate:", g.get_friends("Kate"))
    print("John:", g.get_friends("John"))

    # --------------------------
    # Mutual friends
    # --------------------------
    print("\nMutual friends of Kate and Jake:", common_friends(g, "Kate", "Jake"))

    # --------------------------
    # Ensure friendship exists before updating weight
    # --------------------------
    if "John" not in [f for f, _ in g.get_friends("Kate")]:
        g.add_friend("Kate", "John", weight=5)
    else:
        g.users["Kate"].update_weight("John", 5)
        g.users["John"].update_weight("Kate", 5)

    # Add a new friendship between Jake and Anna
    g.add_friend("Jake", "Anna", weight=2)

    print("\nUpdated friends:")
    print("Kate:", g.get_friends("Kate"))
    print("John:", g.get_friends("John"))
    print("Jake:", g.get_friends("Jake"))
    print("Anna:", g.get_friends("Anna"))

    # --------------------------
    # Shortest path (BFS)
    # --------------------------
    print("\nShortest path Kate → John:", shortest_path(g, "Kate", "John"))

    # --------------------------
    # Friend recommendations (mutual friends)
    # --------------------------
    print("\nFriend recommendations for John:", recommend_friends(g, "John"))

    # --------------------------
    # Weighted friend recommendations
    # --------------------------
    print("\nWeighted friend recommendations for John:", recommend_friends_weighted(g, "John"))

    # --------------------------
    # Shortest weighted path (Dijkstra-like)
    # --------------------------
    print("\nShortest weighted path Kate → John:", shortest_weighted_path(g, "Kate", "John"))


if __name__ == "__main__":
    demo()
