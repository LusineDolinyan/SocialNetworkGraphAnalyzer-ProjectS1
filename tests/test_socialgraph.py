
import unittest
from SocialNetworkGraphAnalyzer.graph import SocialGraph
from SocialNetworkGraphAnalyzer.algorithms import common_friends, shortest_path, recommend_friends

class TestSocialGraph(unittest.TestCase):

    def setUp(self):
        self.g = SocialGraph()
        self.g.add_user("Kate")
        self.g.add_user("John")
        self.g.add_user("Jake")
        self.g.add_user("Anna")

        self.g.add_friend("Kate", "Jake")
        self.g.add_friend("Kate", "John")
        self.g.add_friend("Jake", "John")

    def test_add_user(self):
        self.g.add_user("Bob")
        self.assertIn("Bob", self.g.users)

    def test_remove_user(self):
        self.g.remove_user("Anna")
        self.assertNotIn("Anna", self.g.users)

    def test_add_friend(self):
        self.g.add_friend("Kate", "Anna")
        self.assertIn("Anna", self.g.get_friends("Kate"))
        self.assertIn("Kate", self.g.get_friends("Anna"))

    def test_remove_friend(self):
        self.g.remove_friend("Kate", "John")
        self.assertNotIn("John", self.g.get_friends("Kate"))
        self.assertNotIn("Kate", self.g.get_friends("John"))

    def test_common_friends(self):
        self.assertCountEqual(common_friends(self.g, "Kate", "Jake"), ["John"])

    def test_shortest_path(self):
        path = shortest_path(self.g, "Kate", "John")
        self.assertEqual(path, ["Kate", "John"])

        self.g.remove_friend("Kate", "John")
        path2 = shortest_path(self.g, "Kate", "John")
        self.assertEqual(path2, ["Kate", "Jake", "John"])

    def test_recommend_friends(self):
        rec_kate = recommend_friends(self.g, "Kate")
        self.assertEqual(rec_kate, [])

        self.g.add_friend("Anna", "John")
        rec_anna = recommend_friends(self.g, "Anna")
        self.assertIn( "Jake", rec_anna)


if __name__ == "__main__":
    unittest.main()
