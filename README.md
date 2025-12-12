# SocialNetworkGraphAnalyzer

Analyze social networks with user connections, mutual friends, shortest paths, and friend recommendations.
A clean and lightweight educational project for ProjectS1.

## Features

* Add/remove users
* Add/remove friendships
* Get a user's friends (with weights and optional comments)
* Find mutual friends between users
* Compute the shortest path between users (BFS)
* Recommend friends (based on mutual friends and weighted connections)
* Compute the shortest weighted paths (Dijkstra-like)
* Identify friendship clusters
* Simple graph-based API for educational purposes

---

## Installation

```bash
git clone https://github.com/LusineDolinyan/SocialNetworkGraphAnalyzer-ProjectS1.git
cd SocialNetworkGraphAnalyzer-ProjectS1
```

(Optional) create a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## SocialGraph Class

The main class for managing users and their friendships:

```python
from SocialNetworkGraphAnalyzer.graph import SocialGraph

g = SocialGraph()
g.add_user("Kate")
g.add_user("John")
g.add_friend("Kate", "John", weight=2)
print(g.get_friends("Kate"))  # [('John', 2)]
```

* Friendships have **weights** (integer values) representing connection strength.
* Optional comments can be attached to friendships.
* Provides basic graph operations like add/remove user and add/remove friend.

---

## Quickstart Example

```python
from SocialNetworkGraphAnalyzer.graph import SocialGraph
from SocialNetworkGraphAnalyzer.algorithms import common_friends, shortest_path, recommend_friends

g = SocialGraph()

g.add_user("Kate")
g.add_user("John")
g.add_user("Jake")

g.add_friend("Kate", "Jake")
g.add_friend("Kate", "John")

print("Kate's friends:", g.get_friends("Kate"))

# Remove a friendship
g.remove_friend("Kate", "John")
print("Kate's friends after removal:", g.get_friends("Kate"))

# Find mutual friends
print("Mutual friends of Kate and Jake:", common_friends(g, "Kate", "Jake"))

# Shortest path between users
g.add_friend("Jake", "John")
print("Shortest path Kate → John:", shortest_path(g, "Kate", "John"))

# Friend recommendations
print("Friend recommendations for John:", recommend_friends(g, "John"))
```

---

## Full Demonstration Script

```python
from SocialNetworkGraphAnalyzer.graph import SocialGraph
from SocialNetworkGraphAnalyzer.algorithms import (
    common_friends,
    shortest_path,
    recommend_friends,
    recommend_friends_weighted,
    shortest_weighted_path
)

def demo():
    g = SocialGraph()
    g.add_user("Kate")
    g.add_user("John")
    g.add_user("Jake")
    g.add_user("Anna")

    g.add_friend("Kate", "Jake", weight=1)
    g.add_friend("Kate", "John", weight=2)
    g.add_friend("Jake", "John", weight=3)

    print("Initial friends:")
    print("Kate:", g.get_friends("Kate"))
    print("John:", g.get_friends("John"))
    print("Jake:", g.get_friends("Jake"))

    g.remove_friend("Kate", "John")
    print("\nAfter removing Kate-John friendship:")
    print("Kate:", g.get_friends("Kate"))
    print("John:", g.get_friends("John"))

    print("\nMutual friends of Kate and Jake:", common_friends(g, "Kate", "Jake"))

    # Ensure friendship exists before updating weight
    if "John" not in [f for f, _ in g.get_friends("Kate")]:
        g.add_friend("Kate", "John", weight=5)

    g.add_friend("Jake", "Anna", weight=2)

    print("\nUpdated friends:")
    print("Kate:", g.get_friends("Kate"))
    print("John:", g.get_friends("John"))
    print("Jake:", g.get_friends("Jake"))
    print("Anna:", g.get_friends("Anna"))

    print("\nShortest path Kate → John:", shortest_path(g, "Kate", "John"))
    print("Friend recommendations for John:", recommend_friends(g, "John"))
    print("Weighted friend recommendations for John:", recommend_friends_weighted(g, "John"))
    print("Shortest weighted path Kate → John:", shortest_weighted_path(g, "Kate", "John"))

if __name__ == "__main__":
    demo()
```

---

## Expected Output

```
Initial friends:
Kate: [('Jake', 1), ('John', 2)]
John: [('Kate', 2), ('Jake', 3)]
Jake: [('Kate', 1), ('John', 3)]

After removing Kate-John friendship:
Kate: [('Jake', 1)]
John: [('Jake', 3)]

Mutual friends of Kate and Jake: []

Shortest path Kate → John: ['Kate', 'Jake', 'John']

Friend recommendations for John: ['Kate']
Weighted friend recommendations for John: ['Kate']
Shortest weighted path Kate → John: (['Kate', 'Jake', 'John'], 1.333333...)
```

---

## Why This Project is Useful

* Easy to manage social networks with a simple and intuitive API.
* Quickly identify mutual friends, shortest paths, and friend recommendations.
* Lightweight, minimal setup—just clone, install dependencies, and run.
* Demonstrates graph algorithms and weighted connections in a real-world context.
* Ideal for learning, coursework projects, or educational demonstrations.
