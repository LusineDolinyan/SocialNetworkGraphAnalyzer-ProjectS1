# SocialNetworkGraphAnalyzer

Analyze social networks with user connections, mutual friends, shortest paths, and friend recommendations.
A clean and lightweight educational project for ProjectS1.

## Features

- Add/remove users
- Add/remove friendships
- Get a user's friends
- Mutual friends
- Shortest path between users
- Friend recommendations
- Simple graph-based API


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


## SocialNetwork class

```python
class SocialNetwork:
    def __init__(self):
        self.graph = {}
    ...
```
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
...


```
---
## Full Demonstration Script

```python
from SocialNetworkGraphAnalyzer.graph import SocialGraph
from SocialNetworkGraphAnalyzer.algorithms import common_friends, shortest_path, recommend_friends

def demo():
    ...
if __name__ == "__main__":
    demo()

```

---

## Expected Output

```
Initial friends:
Kate: ['Jake', 'John']
John: ['Kate']
Jake: ['Kate']

After removing Kate-John friendship:
Kate: ['Jake']
John: []

Mutual friends of Kate and Jake: []

Shortest path Kate→John: ['Kate', 'Jake', 'John']

Friend recommendations for John: ['Kate']
```

---

## Why This is Convenient

- Easy to manage social networks with simple API.
- Quickly see mutual friends, shortest paths, and friend recommendations.
- Minimal setup — just clone, install dependencies, and run.
- Demonstrates graph algorithms in action.
- Ideal for learning or coursework projects.









