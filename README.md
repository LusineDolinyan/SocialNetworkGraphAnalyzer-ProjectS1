SocialNetworkGraphAnalyzer

A simple Python project to explore social networks with friend connections, mutual friends, shortest paths, and friend recommendations.

Features

Add and remove users and friendships.

Get a list of friends for any user.

Find mutual friends between users.

Compute shortest paths in the network.

Recommend new friends based on network connections.

Clean and modular API ready for extensions.

Install
# Clone the repository
git clone https://github.com/LusineDolinyan/SocialNetworkGraphAnalyzer-ProjectS1.git
cd SocialNetworkGraphAnalyzer-ProjectS1

# Optional: create virtual environment
python -m venv venv
source venv/Scripts/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt  # if any dependencies


# Optional: create virtual environment
python -m venv venv
source venv/Scripts/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt  # if any dependencies

Quickstart

from SocialNetworkGraphAnalyzer.algorithms import common_friends, shortest_path, recommend_friends
from SocialNetworkGraphAnalyzer.main import SocialGraph

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
print("Mutual friends of Kate and Jake:", common_friends(g, "Kate", "Jake"))
print("Shortest path Kate→John:", shortest_path(g, "Kate", "John"))
print("Recommendations for John:", recommend_friends(g, "John"))

Why this is convenient

Demonstrates core graph algorithms in a social network context.

Modular code: algorithms.py separate from main.py.

Easy to extend with more features like network metrics or visualizations.

Perfect for coursework and showcasing real-time demonstration on oral defense.

About

ProjectS1 assignment for Social Network Graph Analyzer.

Resources

GitHub Repository: SocialNetworkGraphAnalyzer-ProjectS1