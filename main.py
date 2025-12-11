from SocialNetworkGraphAnalyzer.graph import SocialGraph
from SocialNetworkGraphAnalyzer.algorithms import common_friends, shortest_path, recommend_friends

def demo():
    g = SocialGraph()
    g.add_user("Kate")
    g.add_user("John")
    g.add_user("Jake")

    g.add_friend("Kate", "Jake")
    g.add_friend("Kate", "John")

    print("Initial friends:")
    print("Kate:", g.get_friends("Kate"))
    print("John:", g.get_friends("John"))
    print("Jake:", g.get_friends("Jake"))

    g.remove_friend("Kate", "John")
    print("\nAfter removing Kate-John friendship:")
    print("Kate:", g.get_friends("Kate"))
    print("John:", g.get_friends("John"))

    print("\nMutual friends of Kate and Jake:", common_friends(g, "Kate", "Jake"))

    g.add_friend("Jake", "John")
    print("\nShortest path Kate→John:", shortest_path(g, "Kate", "John"))

    print("\nFriend recommendations for John:", recommend_friends(g, "John"))

if __name__ == "__main__":
    demo()
