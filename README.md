# SocialNetworkGraphAnalyzer-ProjectS1

A convenient social network graph analyzer for coursework and real projects:

- Manage users and friendships
- Compute mutual friends
- Recommend new friends
- Find shortest paths between users
- Designed for demonstration and analysis of social graphs

---

## Features

- Add/remove users and friendships
- Query friends of any user
- Compute common friends between users
- Recommend friends based on network connections
- Compute shortest path between users in the social graph
- Easy-to-use Python API

---

## Installation

Make sure you have Python 3.x installed.

Clone the repository:

```bash
git clone https://github.com/LusineDolinyan/SocialNetworkGraphAnalyzer-ProjectS1.git
cd SocialNetworkGraphAnalyzer-ProjectS1

(Optional) Create a virtual environment:

python -m venv venv
source venv/Scripts/activate  # Windows

Install dependencies (if any):

pip install -r requirements.txt


Quickstart

from SocialNetworkGraphAnalyzer.algorithms import common_friends, shortest_path, recommend_friends
from SocialNetworkGraphAnalyzer.graph import SocialGraph

# Initialize graph
g = SocialGraph()
g.add_user("Kate")
g.add_user("John")
g.add_user("Jake")

# Add friendships
g.add_friend("Kate", "Jake")
g.add_friend("Kate", "John")

# Show friends
print("Kate's Friends:", g.get_friends("Kate"))
print("John's Friends:", g.get_friends("John"))
print("Jake's Friends:", g.get_friends("Jake"))

# Remove friendship
g.remove_friend("Kate", "John")
print("\nAfter deleting the Kate-John friendship:")
print("Kate's Friends:", g.get_friends("Kate"))
print("John's Friends:", g.get_friends("John"))

# Mutual friends
print("Mutual friends of Kate and Jake:", common_friends(g, "Kate", "Jake"))

# Add another friendship
g.add_friend("Jake", "John")

# Shortest path
print("Shortest path Kate→John:", shortest_path(g, "Kate", "John"))

# Friend recommendations
print("Recommendations for John:", recommend_friends(g, "John"))



