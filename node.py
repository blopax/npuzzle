import math
import utils

goal = utils.create_goal(3)


class Node:
    def __init__(self, parent=None, moved_tile=None, state=None):
        self.parent = parent
        self.moved_tile = moved_tile
        if parent is None:
            self.cost = 0
            self.state = state
        else:
            self.cost = self.parent.cost + 1
            self.state = utils.action(parent.state, moved_tile)
        self.heuristic = self.heuristic_manhattan(goal)
        self.evaluation = self.cost + self.heuristic
        self.possible_actions = self.find_possible_actions()
        self.finished = (self.state == goal)

    def __str__(self):
        string = """id(parent) = {}
moved_tile = {}
cost = {}
heuristic = {}
evaluation = {}
possible_actions = {}
finished = {}\n""".format(id(self.parent), self.moved_tile,
                          self.cost, self.heuristic, self.evaluation, self.possible_actions, self.finished)
        string += "state =\n{}".format(utils.puzzle_formatted_str(self.state))
        return string

    def find_possible_actions(self) -> list:
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

    def heuristic_manhattan(self, goal):
        manhattan_distance = 0
        size = int(math.sqrt(len(self.state)))
        for index, item in enumerate(self.state):
            item_x = index % size
            item_y = index // size
            goal_index = goal.index(item)
            goal_x = goal_index % size
            goal_y = goal_index // size
            manhattan_distance += abs(item_x - goal_x) + abs(item_y - goal_y)
        return manhattan_distance


if __name__ == "__main__":
    initial_node = Node(None, None, [1, 0, 2, 3, 4, 5, 6, 7, 8])
    print(initial_node.__str__())
    print("goal =\n{}".format(utils.puzzle_formatted_str(utils.create_goal(3))))
    second_node = Node(initial_node, 2, None)
    print(second_node.__str__())
    print("goal =\n{}".format(utils.puzzle_formatted_str(utils.create_goal(3))))
