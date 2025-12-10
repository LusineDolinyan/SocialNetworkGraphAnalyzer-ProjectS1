from SocialNetworkGraphAnalyzer.graph import SocialGraph
from SocialNetworkGraphAnalyzer.algorithms import common_friends, shortest_path, recommend_friends

g = SocialGraph()
g.add_user("Kate")
g.add_user("John")
g.add_user("Jake")

g.add_friend("Kate", "Jake")
g.add_friend("Kate", "John")

print("Kate's Friends:", g.get_friends("Kate"))
print("John's Friends:", g.get_friends("John"))
print("Jake's Friends:", g.get_friends("Jake"))

g.remove_friend("Kate", "John")

print("\nAfter deleting the Kate-John friendship:")
print("Kate's Friends:", g.get_friends("Kate"))
print("John's Friends:", g.get_friends("John"))

print("Mutual friends of Kate and Jake:", common_friends(g, "Kate", "Jake"))

g.add_friend("Jake", "John")

print("Shortest path  Kate→John:", shortest_path(g, "Kate", "John"))

print("Recommendations for John:", recommend_friends(g, "John"))