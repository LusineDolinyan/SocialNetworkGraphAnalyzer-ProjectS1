from collections import deque

def common_friends(graph, user1, user2):
    if user1 not in graph.users or user2 not in graph.users:
        raise ValueError("One of the users was not found.")
    return list(graph.users[user1].friends & graph.users[user2].friends)


def shortest_path(graph, start, end):
    if start not in graph.users or end not in graph.users:
        raise ValueError("User not found.")
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return  path
        if node not in visited:
            visited.add(node)
            for friend in graph.users[node].friends:
                new_path = list(path)
                new_path.append(friend)
                queue.append(new_path)
    return None


def recommend_friends(graph, user_name):
    if user_name not in graph.users:
        raise ValueError("User not found")

    user_friends = graph.users[user_name].friends
    recommendations = {}


    for friend in user_friends:
        for fof in graph.users[friend].friends:
            if fof != user_name and fof not in user_friends:
                recommendations[fof] = recommendations.get(fof, 0) + 1

    return sorted(recommendations, key=lambda x: recommendations[x], reverse = True)

