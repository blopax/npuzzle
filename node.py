import math
import utils


# TODO goal mettre var globale heuristique manhattan = math.fabs(x - x.goal) + math.fabs(y - y.goal)

class Node:
    def __init__(self, parent=None, moved_tile=None, state=None, goal=None):
        self.parent = parent
        self.moved_tile = moved_tile
        if parent is None:
            self.cost = 0
            self.state = state
        else:
            self.cost = self.parent.cost + 1
            self.state = utils.action(parent.state, moved_tile)
        if goal is None:
            self.goal = parent.goal
        else:
            self.goal = goal
        self.heuristic = self.heuristic_misplaced(self.goal)
        self.evaluation = self.cost + self.heuristic
        self.possible_actions = self.find_possible_actions()

    def __str__(self):
        string = """id(parent) = {}
moved_tile = {}
cost = {}
heuristic = {}
evaluation = {}
possible_actions = {}\n""".format(id(self.parent), self.moved_tile,
                                  self.cost, self.heuristic, self.evaluation, self.possible_actions)
        string += "state =\n{}".format(utils.puzzle_formatted_str(self.state))
        return string

    def find_possible_actions(self):
        possible_actions = []
        zero_index = None
        size = int(math.sqrt(len(self.state)))
        for index, item in enumerate(self.state):
            if item == 0:
                zero_index = index
                break
        zero_x = zero_index % size
        zero_y = zero_index // size
        if zero_x - 1 >= 0:
            possible_actions.append(self.state[zero_y * size + zero_x - 1])
        if zero_x + 1 < size:
            possible_actions.append(self.state[zero_y * size + zero_x + 1])
        if zero_y - 1 >= 0:
            possible_actions.append(self.state[(zero_y - 1) * size + zero_x])
        if zero_y + 1 < size:
            possible_actions.append(self.state[(zero_y + 1) * size + zero_x])
        if self.moved_tile:
            possible_actions.remove(self.moved_tile)
        return possible_actions

    def heuristic_misplaced(self, goal):
        misplaced_tiles = 0
        for index, item in enumerate(self.state):
            if item != 0 and item != goal[index]:
                misplaced_tiles += 1
        return misplaced_tiles


if __name__ == "__main__":
    initial_node = Node(None, None, [1, 0, 2, 3, 4, 5, 6, 7, 8], utils.create_goal(3))
    print(initial_node.__str__())
    print("goal =\n{}".format(utils.puzzle_formatted_str(utils.create_goal(3))))
    second_node = Node(initial_node, 2, None, None)
    print(second_node.__str__())
    print("goal =\n{}".format(utils.puzzle_formatted_str(utils.create_goal(3))))



Algo
List+noeuds_crees --> ordonnera en fonction evaluation

