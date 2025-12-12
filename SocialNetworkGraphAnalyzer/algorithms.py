from collections import deque
import heapq

# -------------------------
# ALGORITHMS
# -------------------------

def common_friends(graph, user1, user2):
    # Returns a list of common friends between two users
    if user1 not in graph.users or user2 not in graph.users:
        raise ValueError("One of the users was not found.")

    f1 = set(graph.users[user1].friends.keys())  # Set of user1's friends
    f2 = set(graph.users[user2].friends.keys())  # Set of user2's friends
    return list(f1 & f2)  # Intersection of friend sets


def shortest_path(graph, start, end):
    # Returns the shortest path (in terms of number of connections) between start and end using BFS
    if start not in graph.users or end not in graph.users:
        raise ValueError("User not found.")

    queue = deque([[start]])  # Queue of paths to explore
    visited = set()  # Track visited nodes to prevent cycles

    while queue:
        path = queue.popleft()  # Get the first path in the queue
        node = path[-1]  # Current node

        if node == end:
            return path  # Return path if destination reached

        if node not in visited:
            visited.add(node)
            for friend in graph.users[node].friends.keys():
                queue.append(path + [friend])  # Add new path including friend

    return []  # Return empty list if no path found


def recommend_friends(graph, user_name):
    # Recommends friends for a user based on mutual friends
    if user_name not in graph.users:
        raise ValueError("User not found")

    user_friends = set(graph.users[user_name].friends.keys())  # Current friends
    rec = {}  # Dictionary to count mutual friend occurrences

    for friend in user_friends:
        for fof in graph.users[friend].friends.keys():  # Friends of friends
            if fof != user_name and fof not in user_friends:
                rec[fof] = rec.get(fof, 0) + 1  # Increment count for recommendation

    # Return recommended friends sorted by number of mutual friends (descending)
    return sorted(rec, key=lambda x: rec[x], reverse=True)


def strongest_friends(graph, user, top_n=3):
    # Returns top_n friends with the strongest connection weights
    if user not in graph.users:
        raise ValueError("User not found")

    friends = graph.users[user].friends.items()  # Get friends and weights
    return sorted(friends, key=lambda x: x[1], reverse=True)[:top_n]  # Sort by weight


def recommend_friends_weighted(graph, user_name):
    # Weighted friend recommendation based on connection strengths
    if user_name not in graph.users:
        raise ValueError("User not found")

    user_friends = graph.users[user_name].friends  # Dictionary of friends and weights
    rec = {}

    for friend, w in user_friends.items():
        for fof in graph.users[friend].friends.keys():  # Friends of friends
            if fof != user_name and fof not in user_friends:
                rec[fof] = rec.get(fof, 0) + w  # Add weight instead of just count

    # Return recommendations sorted by weight descending, then by name
    return sorted(rec, key=lambda x: (-rec[x], x))


def shortest_weighted_path(graph, start, end):
    # Finds the shortest path considering weighted edges using Dijkstra-like approach
    if start not in graph.users or end not in graph.users:
        raise ValueError("User not found.")

    pq = [(0, start, [start])]  # Priority queue of (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)  # Get node with lowest cost

        if node == end:
            return path, cost  # Return path and total cost

        if node in visited:
            continue
        visited.add(node)

        for friend, weight in graph.users[node].friends.items():
            # Calculate new cost; prevent division by zero with large number
            new_cost = cost + (1 / weight if weight > 0 else 999999)
            heapq.heappush(pq, (new_cost, friend, path + [friend]))

    return [], float("inf")  # Return empty path if no path found


def friendship_clusters(graph):
    # Returns all clusters of connected users in the graph
    visited = set()
    clusters = []

    for user in graph.users:
        if user not in visited:
            stack = [user]  # DFS stack
            cluster = []  # Users in current cluster

            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    cluster.append(node)
                    stack.extend(graph.users[node].friends.keys())  # Add friends to stack

            clusters.append(cluster)  # Add completed cluster

    return clusters
