import unittest
from SocialNetworkGraphAnalyzer.graph import SocialGraph
from SocialNetworkGraphAnalyzer.algorithms import (
    common_friends,
    shortest_path,
    recommend_friends,
    strongest_friends,
    recommend_friends_weighted,
    shortest_weighted_path,
    friendship_clusters
)

# Helper: extract only friend names from get_friends() results
def friend_names(friend_list):
    return [name for name, _ in friend_list]


class TestSocialGraph(unittest.TestCase):

    def setUp(self):
        self.g = SocialGraph()
        self.g.add_user("Kate")
        self.g.add_user("John")
        self.g.add_user("Jake")
        self.g.add_user("Anna")

        self.g.add_friend("Kate", "Jake", weight=1)
        self.g.add_friend("Kate", "John", weight=1)
        self.g.add_friend("Jake", "John", weight=1)

    # --------------------------
    # FUNCTIONALITY TESTS
    # --------------------------

    def test_add_user(self):
        self.g.add_user("Bob")
        self.assertIn("Bob", self.g.users)

    def test_remove_user(self):
        self.g.remove_user("Anna")
        self.assertNotIn("Anna", self.g.users)

    def test_remove_nonexistent_user(self):
        with self.assertRaises(ValueError):
            self.g.remove_user("Sara")

    def test_add_friend(self):
        self.g.add_friend("Kate", "Anna", weight=3)
        self.assertIn("Anna", friend_names(self.g.get_friends("Kate")))
        self.assertIn("Kate", friend_names(self.g.get_friends("Anna")))

    def test_remove_friend(self):
        self.g.remove_friend("Kate", "John")
        self.assertNotIn("John", friend_names(self.g.get_friends("Kate")))
        self.assertNotIn("Kate", friend_names(self.g.get_friends("John")))

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

        self.g.add_friend("Anna", "John", weight=2)
        rec_anna = recommend_friends(self.g, "Anna")
        self.assertIn("Jake", rec_anna)

    def test_strongest_friends(self):
        # change weights so ordering is clear
        self.g.users["Kate"].update_weight("John", 5)
        self.g.users["Kate"].update_weight("Jake", 2)

        top2 = strongest_friends(self.g, "Kate", top_n=2)
        self.assertEqual(top2[0], ("John", 5))
        self.assertEqual(top2[1], ("Jake", 2))

    def test_recommend_friends_weighted(self):
        # Anna -> John (weight 2); John -> Jake exists
        self.g.add_friend("Anna", "John", weight=2)
        # weighted recommendation should include Jake
        rec = recommend_friends_weighted(self.g, "Anna")
        self.assertIn("Jake", rec)

        # if we increase Anna->John weight, Jake score increases (ordering)
        self.g.users["Anna"].update_weight("John", 10)
        rec2 = recommend_friends_weighted(self.g, "Anna")
        self.assertEqual(rec2[0], "Jake")

    def test_shortest_weighted_path(self):
        # Make direct Kate-John weak and via Jake strong so weighted path prefers via Jake
        self.g.users["Kate"].update_weight("John", 1)   # cost 1.0
        self.g.users["Kate"].update_weight("Jake", 5)   # cost 0.2
        self.g.users["Jake"].update_weight("John", 5)   # cost 0.2

        path, cost = shortest_weighted_path(self.g, "Kate", "John")
        self.assertEqual(path, ["Kate", "Jake", "John"])
        # cost should be approximately 0.4 (0.2 + 0.2)
        self.assertAlmostEqual(cost, 0.4, places=6)

    def test_friendship_clusters(self):
        # current graph is one connected component among Kate, John, Jake, Anna (Anna isolated unless linked)
        # create a separate cluster
        self.g.add_user("Bob")
        self.g.add_user("Carol")
        self.g.add_friend("Bob", "Carol", weight=1)

        clusters = friendship_clusters(self.g)
        # convert clusters to sets for easier assertions
        cluster_sets = [set(c) for c in clusters]

        # there should be at least one cluster containing Bob and Carol together
        self.assertTrue(any({"Bob", "Carol"}.issubset(cs) for cs in cluster_sets))

    # --------------------------
    # EDGE CASE TESTS
    # --------------------------

    def test_add_existing_user(self):
        with self.assertRaises(ValueError):
            self.g.add_user("Kate")

    def test_add_friend_user_not_found(self):
        with self.assertRaises(ValueError):
            self.g.add_friend("Kate", "XYZ")

    def test_remove_friend_user_not_found(self):
        with self.assertRaises(ValueError):
            self.g.remove_friend("Kate", "Ghost")

    def test_get_friends_of_nonexistent_user(self):
        with self.assertRaises(ValueError):
            self.g.get_friends("GhostUser")

    def test_shortest_path_disconnected(self):
        self.g.remove_user("Anna")
        self.g.add_user("Anna")  # isolated again

        path = shortest_path(self.g, "Kate", "Anna")
        self.assertEqual(path, [])

    def test_common_friends_no_overlap(self):
        self.assertEqual(common_friends(self.g, "Anna", "Kate"), [])

    def test_recommend_friends_no_options(self):
        self.g.add_friend("Anna", "Kate", weight=1)
        self.g.add_friend("Anna", "Jake", weight=1)
        self.g.add_friend("Anna", "John", weight=1)

        rec = recommend_friends(self.g, "Anna")
        self.assertEqual(rec, [])

    def test_graph_repr(self):
        rep = repr(self.g)
        self.assertIn("SocialGraph", rep)

    def test_remove_user_cleans_friendships(self):
        self.g.remove_user("Kate")
        self.assertNotIn("Kate", friend_names(self.g.get_friends("Jake")))
        self.assertNotIn("Kate", friend_names(self.g.get_friends("John")))


if __name__ == "__main__":
    unittest.main()
