import unittest
import node
import utils


class TestNPuzzle(unittest.TestCase):
    def test_heuristic_misplaced(self):
        size = 2
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [1, 0, 2, 3], None, size, goal)
        self.assertEqual(test_node.heuristic_misplaced(), 1)
        test_node = node.Node(None, None, [0, 3, 2, 1], None, size, goal)
        self.assertEqual(test_node.heuristic_misplaced(), 3)
        test_node = node.Node(None, None, [1, 2, 0, 3], None, size, goal)
        self.assertEqual(test_node.heuristic_misplaced(), 0)
        test_node = node.Node(None, None, [0, 1, 2, 3], None, size, goal)
        self.assertEqual(test_node.heuristic_misplaced(), 2)

        size = 3
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [1, 0, 2, 3, 4, 5, 6, 7, 8], None, size, goal)
        self.assertEqual(test_node.heuristic_misplaced(), 7)
        test_node = node.Node(None, None, goal, None, size, goal)
        self.assertEqual(test_node.heuristic_misplaced(), 0)
        test_node = node.Node(None, None, [1, 2, 3, 0, 4, 5, 6, 7, 8], None, size, goal)
        self.assertEqual(test_node.heuristic_misplaced(), 5)
        test_node = node.Node(None, None, [1, 0, 2, 8, 4, 5, 7, 6, 3], None, size, goal)
        self.assertEqual(test_node.heuristic_misplaced(), 4)

        size = 4
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], None, size, goal)
        self.assertEqual(test_node.heuristic_misplaced(), 15)
        test_node = node.Node(None, None, goal, None, size, goal)
        self.assertEqual(test_node.heuristic_misplaced(), 0)

    def test_heuristic_manhattan(self):
        size = 2
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [1, 0, 2, 3], None, size, goal)
        self.assertEqual(test_node.heuristic_manhattan(), 2)
        test_node = node.Node(None, None, [0, 3, 2, 1], None, size, goal)
        self.assertEqual(test_node.heuristic_manhattan(), 5)
        test_node = node.Node(None, None, [1, 2, 0, 3], None, size, goal)
        self.assertEqual(test_node.heuristic_manhattan(), 0)
        test_node = node.Node(None, None, [0, 1, 2, 3], None, size, goal)
        self.assertEqual(test_node.heuristic_manhattan(), 3)

        size = 3
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [1, 0, 2, 3, 4, 5, 6, 7, 8], None, size, goal)
        self.assertEqual(test_node.heuristic_manhattan(), 11)
        test_node = node.Node(None, None, goal, None, size, goal)
        self.assertEqual(test_node.heuristic_manhattan(), 0)
        test_node = node.Node(None, None, [1, 2, 3, 0, 4, 5, 6, 7, 8], None, size, goal)
        self.assertEqual(test_node.heuristic_manhattan(), 7)
        test_node = node.Node(None, None, [1, 0, 2, 8, 4, 5, 7, 6, 3], None, size, goal)
        self.assertEqual(test_node.heuristic_manhattan(), 5)

        size = 4
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], None, size, goal)
        self.assertEqual(test_node.heuristic_manhattan(), 31)
        test_node = node.Node(None, None, goal, None, size, goal)
        self.assertEqual(test_node.heuristic_manhattan(), 0)

    def test_improved_heuristic_manhattan(self):
        size = 2
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [1, 0, 2, 3], None, size, goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(), 2)
        test_node = node.Node(None, None, [0, 3, 2, 1], None, size, goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(), 5)
        test_node = node.Node(None, None, [1, 2, 0, 3], None, size, goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(), 0)
        test_node = node.Node(None, None, [0, 1, 2, 3], None, size, goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(), 3)

        size = 3
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [1, 0, 2, 3, 4, 5, 6, 7, 8], None, size, goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(), 13)
        test_node = node.Node(None, None, goal, None, size, goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(), 0)
        test_node = node.Node(None, None, [1, 2, 3, 0, 4, 5, 6, 7, 8], None, size, goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(), 9)
        test_node = node.Node(None, None, [1, 0, 2, 8, 4, 5, 7, 6, 3], None, size, goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(), 7)

        size = 4
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], None, size, goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(), 33)
        test_node = node.Node(None, None, goal, None, size, goal)
        self.assertEqual(test_node.improved_heuristic_manhattan(), 0)

    def test_find_possible_actions(self):
        size = 2
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [0, 3, 2, 1], None, size, goal)
        self.assertEqual(test_node.find_possible_actions(), [3, 2])
        test_node = node.Node(None, None, [1, 2, 0, 3], None, size, goal)
        self.assertEqual(test_node.find_possible_actions(), [3, 1])
        test_node = node.Node(None, 2, [0, 1, 2, 3], None, size, goal)
        self.assertEqual(test_node.find_possible_actions(), [1])

        size = 3
        goal = utils.create_goal(size)
        test_node = node.Node(None, None, [1, 0, 2, 3, 4, 5, 6, 7, 8], None, size, goal)
        self.assertEqual(test_node.find_possible_actions(), [1, 2, 4])
        test_node = node.Node(None, None, [1, 2, 3, 0, 4, 5, 6, 7, 8], None, size, goal)
        self.assertEqual(test_node.find_possible_actions(), [4, 1, 6])
        test_node = node.Node(None, 1, [1, 0, 2, 8, 4, 5, 7, 6, 3], None, size, goal)
        self.assertEqual(test_node.find_possible_actions(), [2, 4])

        size = 4
        goal = utils.create_goal(size)
        test_node = node.Node(None, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15], None, size, goal)
        self.assertEqual(test_node.find_possible_actions(), [9, 10, 13])

    def test_create_goal(self):
        size = 2
        goal = utils.create_goal(size)
        self.assertEqual(goal, [1, 2, 0, 3])

        size = 3
        goal = utils.create_goal(size)
        self.assertEqual(goal, [1, 2, 3, 8, 0, 4, 7, 6, 5])

        size = 4
        goal = utils.create_goal(size)
        self.assertEqual(goal, [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7])

    def test_action(self):
        puzzle = [0, 1, 2, 3]
        action = 1
        self.assertEqual(utils.action(puzzle, action), [1, 0, 2, 3])

        puzzle = [0, 1, 2, 3]
        action = 2
        self.assertEqual(utils.action(puzzle, action), [2, 1, 0, 3])

        puzzle = [0, 1, 2, 3]
        action = 3
        with self.assertRaises(Exception):
            utils.action(puzzle, action)

        puzzle = [0, 1, 2, 3]
        action = -1
        with self.assertRaises(Exception):
            utils.action(puzzle, action)

    def test_puzzle_has_snail_solution(self):
        puzzle = [0, 1, 2, 3, 5, 4, 7, 6, 8]
        self.assertEqual(utils.puzzle_has_solution(puzzle, 'snail'), False)
        self.assertEqual(utils.puzzle_has_solution(puzzle, 'classic'), True)

        puzzle = [0, 1, 3, 2, 4, 5, 6, 7, 8]
        self.assertEqual(utils.puzzle_has_solution(puzzle, 'snail'), True)
        self.assertEqual(utils.puzzle_has_solution(puzzle, 'classic'), False)

        puzzle = [4, 1, 2, 3, 8, 5, 6, 7, 0, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(utils.puzzle_has_solution(puzzle, 'snail'), False)
        self.assertEqual(utils.puzzle_has_solution(puzzle, 'classic'), True)

        puzzle = [8, 1, 2, 3, 4, 5, 6, 7, 0, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(utils.puzzle_has_solution(puzzle, 'snail'), True)
        self.assertEqual(utils.puzzle_has_solution(puzzle, 'classic'), False)


if __name__ == "__main__":
    unittest.main()
