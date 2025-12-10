# SocialNetworkGraphAnalyzer-ProjectS1

A Python project for analyzing social networks: managing friendships, finding mutual friends, computing shortest paths, and recommending friends. This project is designed for coursework and demonstrates working functionalities in real-time.

---

## Table of Contents
1. [Overview](#overview)  
2. [Installation](#installation)  
3. [Quickstart](#quickstart)  
4. [Features](#features)  
5. [Project Structure](#project-structure)  
6. [License](#license)  

---

## Overview

This project allows users to:  
- Add and remove users and friendships.  
- Get a list of mutual friends.  
- Compute the shortest path between any two users.  
- Recommend friends based on existing connections.  

It is implemented in Python and uses modular code to separate algorithms from the main application logic.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/LusineDolinyan/SocialNetworkGraphAnalyzer-ProjectS1.git
cd SocialNetworkGraphAnalyzer-ProjectS1


```
## Quickstart
from SocialNetworkGraphAnalyzer.algorithms import common_friends, shortest_path, recommend_friends
from SocialNetworkGraphAnalyzer.graph import SocialGraph

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

print("Shortest path Kate→John:", shortest_path(g, "Kate", "John"))

print("Recommendations for John:", recommend_friends(g, "John"))

---
## Example Output

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

