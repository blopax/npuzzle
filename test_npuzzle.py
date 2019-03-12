import unittest
import algo
import node
import utils


class TestNPuzzle(unittest.TestCase):
    def test_heuristic_misplaced(self):
        algo.size = 2
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [1, 0, 2, 3])
        self.assertEqual(test_node.heuristic_misplaced(algo.goal), 1)
        test_node = node.Node(None, None, [0, 3, 2, 1])
        self.assertEqual(test_node.heuristic_misplaced(algo.goal), 3)
        test_node = node.Node(None, None, [1, 2, 0, 3])
        self.assertEqual(test_node.heuristic_misplaced(algo.goal), 0)
        test_node = node.Node(None, None, [0, 1, 2, 3])
        self.assertEqual(test_node.heuristic_misplaced(algo.goal), 2)

        algo.size = 3
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [1, 0, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(test_node.heuristic_misplaced(algo.goal), 7)
        test_node = node.Node(None, None, algo.goal)
        self.assertEqual(test_node.heuristic_misplaced(algo.goal), 0)
        test_node = node.Node(None, None, [1, 2, 3, 0, 4, 5, 6, 7, 8])
        self.assertEqual(test_node.heuristic_misplaced(algo.goal), 5)
        test_node = node.Node(None, None, [1, 0, 2, 8, 4, 5, 7, 6, 3])
        self.assertEqual(test_node.heuristic_misplaced(algo.goal), 4)

        algo.size = 4
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(test_node.heuristic_misplaced(algo.goal), 15)
        test_node = node.Node(None, None, algo.goal)
        self.assertEqual(test_node.heuristic_misplaced(algo.goal), 0)

    def test_heuristic_manhattan(self):
        algo.size = 2
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [1, 0, 2, 3])
        self.assertEqual(test_node.heuristic_manhattan(algo.goal), 2)
        test_node = node.Node(None, None, [0, 3, 2, 1])
        self.assertEqual(test_node.heuristic_manhattan(algo.goal), 5)
        test_node = node.Node(None, None, [1, 2, 0, 3])
        self.assertEqual(test_node.heuristic_manhattan(algo.goal), 0)
        test_node = node.Node(None, None, [0, 1, 2, 3])
        self.assertEqual(test_node.heuristic_manhattan(algo.goal), 3)

        algo.size = 3
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [1, 0, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(test_node.heuristic_manhattan(algo.goal), 11)
        test_node = node.Node(None, None, algo.goal)
        self.assertEqual(test_node.heuristic_manhattan(algo.goal), 0)
        test_node = node.Node(None, None, [1, 2, 3, 0, 4, 5, 6, 7, 8])
        self.assertEqual(test_node.heuristic_manhattan(algo.goal), 7)
        test_node = node.Node(None, None, [1, 0, 2, 8, 4, 5, 7, 6, 3])
        self.assertEqual(test_node.heuristic_manhattan(algo.goal), 5)

        algo.size = 4
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(test_node.heuristic_manhattan(algo.goal), 31)
        test_node = node.Node(None, None, algo.goal)
        self.assertEqual(test_node.heuristic_manhattan(algo.goal), 0)

    def test_improved_heuristic_manhattan(self):
        algo.size = 2
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [1, 0, 2, 3])
        self.assertEqual(test_node.improved_heuristic_manhattan(algo.goal), 2)
        test_node = node.Node(None, None, [0, 3, 2, 1])
        self.assertEqual(test_node.improved_heuristic_manhattan(algo.goal), 5)
        test_node = node.Node(None, None, [1, 2, 0, 3])
        self.assertEqual(test_node.improved_heuristic_manhattan(algo.goal), 0)
        test_node = node.Node(None, None, [0, 1, 2, 3])
        self.assertEqual(test_node.improved_heuristic_manhattan(algo.goal), 3)

        algo.size = 3
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [1, 0, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(test_node.improved_heuristic_manhattan(algo.goal), 13)
        test_node = node.Node(None, None, algo.goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(algo.goal), 0)
        test_node = node.Node(None, None, [1, 2, 3, 0, 4, 5, 6, 7, 8])
        self.assertEqual(test_node.improved_heuristic_manhattan(algo.goal), 9)
        test_node = node.Node(None, None, [1, 0, 2, 8, 4, 5, 7, 6, 3])
        self.assertEqual(test_node.improved_heuristic_manhattan(algo.goal), 7)

        algo.size = 4
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(test_node.improved_heuristic_manhattan(algo.goal), 33)
        test_node = node.Node(None, None, algo.goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(algo.goal), 0)

    def test_find_possible_actions(self):
        algo.size = 2
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [0, 3, 2, 1])
        self.assertEqual(test_node.find_possible_actions(), [3, 2])
        test_node = node.Node(None, None, [1, 2, 0, 3])
        self.assertEqual(test_node.find_possible_actions(), [3, 1])
        test_node = node.Node(None, 2, [0, 1, 2, 3])
        self.assertEqual(test_node.find_possible_actions(), [1])

        algo.size = 3
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, None, [1, 0, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(test_node.find_possible_actions(), [1, 2, 4])
        test_node = node.Node(None, None, [1, 2, 3, 0, 4, 5, 6, 7, 8])
        self.assertEqual(test_node.find_possible_actions(), [4, 1, 6])
        test_node = node.Node(None, 1, [1, 0, 2, 8, 4, 5, 7, 6, 3])
        self.assertEqual(test_node.find_possible_actions(), [2, 4])

        algo.size = 4
        algo.goal = utils.create_goal(algo.size)
        test_node = node.Node(None, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15])
        print(test_node.state)
        self.assertEqual(test_node.find_possible_actions(), [9, 10, 13])


if __name__ == "__main__":
    unittest.main()