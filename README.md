# Social Network Graph Analyzer

A Python library for creating and analyzing social networks.
It supports users, friendships, path finding, mutual friends, and intelligent recommendations.


This project was created for educational and practical purposes as part of the Project S1 series.


#  Features

- Create and manage users  
- Add and remove friendships  
- Analyze graph structure  
...
## Usage example

```python
from SocialNetworkGraphAnalyzer.graph import SocialGraph

g = SocialGraph()
g.add_user("Kate")
g.add_user("John")
g.add_friend("Kate", "John")

print(g.get_friends("Kate"))