import matplotlib.pyplot as plt
import networkx as nx
from SocialNetworkGraphAnalyzer.graph import SocialGraph

def visualize_graph(graph: SocialGraph):
    G = nx.Graph()

    # Add nodes
    for user in graph.graph:
        G.add_node(user)

    # Add edges (friendships)
    for user, friends in graph.graph.items():
        for f in friends:
            if not G.has_edge(user, f):
                G.add_edge(user, f)

    plt.figure(figsize=(7, 5))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G, pos,
        with_labels=True,
        node_color="skyblue",
        node_size=1200,
        font_size=10,
        edge_color="gray"
    )

    plt.title("Social Network Graph")
    plt.show()


if __name__ == "__main__":
    g = SocialGraph()

    # Example network
    g.add_user("Kate")
    g.add_user("John")
    g.add_user("Jake")

    g.add_friend("Kate", "Jake")
    g.add_friend("Kate", "John")
    g.add_friend("Jake", "John")

    visualize_graph(g)
