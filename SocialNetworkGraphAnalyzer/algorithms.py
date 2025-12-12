from collections import deque
import heapq

# -------------------------
# ALGORITHMS
# -------------------------

def common_friends(graph, user1, user2):
    if user1 not in graph.users or user2 not in graph.users:
        raise ValueError("One of the users was not found.")

    f1 = set(graph.users[user1].friends.keys())
    f2 = set(graph.users[user2].friends.keys())
    return list(f1 & f2)


def shortest_path(graph, start, end):
    if start not in graph.users or end not in graph.users:
        raise ValueError("User not found.")

    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for friend in graph.users[node].friends.keys():
                queue.append(path + [friend])

    return []


def recommend_friends(graph, user_name):
    if user_name not in graph.users:
        raise ValueError("User not found")

    user_friends = set(graph.users[user_name].friends.keys())
    rec = {}

    for friend in user_friends:
        for fof in graph.users[friend].friends.keys():
            if fof != user_name and fof not in user_friends:
                rec[fof] = rec.get(fof, 0) + 1

    return sorted(rec, key=lambda x: rec[x], reverse=True)


def strongest_friends(graph, user, top_n=3):
    if user not in graph.users:
        raise ValueError("User not found")

    friends = graph.users[user].friends.items()
    return sorted(friends, key=lambda x: x[1], reverse=True)[:top_n]



def recommend_friends_weighted(graph, user_name):
    if user_name not in graph.users:
        raise ValueError("User not found")

    user_friends = graph.users[user_name].friends
    rec = {}

    for friend, w in user_friends.items():
        for fof in graph.users[friend].friends.keys():
            if fof != user_name and fof not in user_friends:
                rec[fof] = rec.get(fof, 0) + w

    return sorted(rec, key=lambda x: (-rec[x], x))

def shortest_weighted_path(graph, start, end):
    if start not in graph.users or end not in graph.users:
        raise ValueError("User not found.")

    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == end:
            return path, cost

        if node in visited:
            continue
        visited.add(node)

        for friend, weight in graph.users[node].friends.items():
            new_cost = cost + (1 / weight if weight > 0 else 999999)
            heapq.heappush(pq, (new_cost, friend, path + [friend]))

    return [], float("inf")


def friendship_clusters(graph):
    visited = set()
    clusters = []

    for user in graph.users:
        if user not in visited:
            stack = [user]
            cluster = []

            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    cluster.append(node)
                    stack.extend(graph.users[node].friends.keys())

            clusters.append(cluster)

    return clusters
