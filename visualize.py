import matplotlib.pyplot as plt
import networkx as nx
from SocialNetworkGraphAnalyzer.graph import SocialGraph


def visualize_graph(graph: SocialGraph):
    G = nx.Graph()

    # Add nodes (each username)
    for username in graph.users.keys():
        G.add_node(username)

    # Add edges with weights (friendship strength)
    for username, user_obj in graph.users.items():
        for friend, weight in user_obj.friends.items():
            # Avoid adding duplicated edges
            if not G.has_edge(username, friend):
                G.add_edge(username, friend, weight=weight)

    # Draw graph
    plt.figure("Visualization", figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)

    # Edge widths proportional to friendship weights
    edges = G.edges(data=True)
    edge_weights = [d["weight"] for _, _, d in edges]

    nx.draw(
        G, pos,
        with_labels=True,
        node_color="skyblue",
        node_size=1200,
        font_size=10,
        edge_color="gray",
        width=edge_weights
    )

    # Optionally, show weight labels on edges
    edge_labels = {(u, v): d["weight"] for u, v, d in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Social Network Graph (Weighted Friendships)")
    plt.show()


if __name__ == "__main__":
    g = SocialGraph()

    # Example network with weights
    g.add_user("Kate")
    g.add_user("John")
    g.add_user("Jake")
    g.add_user("Anna")

    g.add_friend("Kate", "Jake", weight=3)
    g.add_friend("Kate", "John", weight=5)
    g.add_friend("Jake", "John", weight=2)
    g.add_friend("Anna", "John", weight=4)

    visualize_graph(g)
