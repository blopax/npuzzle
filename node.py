import math
import utils


class Node:
    def __init__(self, parent=None, moved_tile=None, state=None, heuristic_kind=None, size=None, goal=None):
        self.parent = parent
        self.moved_tile = moved_tile
        if parent is None:
            self.cost = 0
            self.heuristic_kind = heuristic_kind
            self.size = size
            self.goal = goal
        else:
            self.cost = self.parent.cost + 1
            self.heuristic_kind = self.parent.heuristic_kind
            self.size = self.parent.size
            self.goal = self.parent.goal
        if state is None:
            self.state = utils.action(parent.state, moved_tile)
        else:
            self.state = state
        if self.heuristic_kind == 'improved_manhattan':
            self.heuristic = self.improved_heuristic_manhattan()
        elif self.heuristic_kind == 'manhattan':
            self.heuristic = self.heuristic_manhattan()
        else:
            self.heuristic = self.heuristic_misplaced()
        self.evaluation = self.cost + self.heuristic
        self.possible_actions = self.find_possible_actions()
        self.finished = (self.state == self.goal)

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
        """
        For the state of the node, give the list of the tiles that are possible to swap. Doesn't count the tile that
        has just been moved to arrive to the node.
        :return list: list of int corresponding to the tiles that can be moved.
        """
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

    def heuristic_misplaced(self) -> int:
        """
        Simple consistent heuristic that counts the number of misplaced tiles.
        :return int misplaced tiles: Nb of misplaced tiles
        """
        misplaced_tiles = 0
        for index, item in enumerate(self.state):
            if item != 0 and item != self.goal[index]:
                misplaced_tiles += 1
        return misplaced_tiles

    def heuristic_manhattan(self) -> int:
        """
        Manhattan distance is another consistent heuristic. Count the number move that any tile (but the 0 one) needs
        to get to goal_position, and sums it for all the tiles.
        :return int manhattan_distance:
        """
        manhattan_distance = 0
        size = int(math.sqrt(len(self.state)))
        for index, item in enumerate(self.state):
            if item != 0:
                item_x = index % size
                item_y = index // size
                goal_index = self.goal.index(item)
                goal_x = goal_index % size
                goal_y = goal_index // size
                manhattan_distance += abs(item_x - goal_x) + abs(item_y - goal_y)
        return manhattan_distance

    def improved_heuristic_manhattan(self) -> int:
        """
        Improve heuristic manhattan by adding 2 each time 2 tiles are on their final line or column but in the inverse
        position they should be. (In this case one of the tile has to move to let the other pass and then come back
        to the correct line/column. This heuristic is also consistent.
        :return int distance: heuristic
        """
        distance = self.heuristic_manhattan()
        for index in range(self.size):
            line = self.state[index * self.size: (index + 1) * self.size]
            goal_line = self.goal[index * self.size: (index + 1) * self.size]
            column = [self.state[i] for i in [index + j * self.size for j in range(self.size)]]
            goal_column = [self.goal[i] for i in [index + j * self.size for j in range(self.size)]]
            distance += 2 * (self.inversed_tiles(line, goal_line) + self.inversed_tiles(column, goal_column))
        return distance

    @staticmethod
    def inversed_tiles(line, goal_line) -> int:
        """
        On a given line (or column) count the number of tiles that are on their goal_line (or goal_column) but that
        will need to move from this line (column).
        :param list line:
        :param list goal_line:
        :return int inversed_tiles:
        """
        inversed_tiles = 0
        items_on_correct_line = set(line) & set(goal_line) - {0}
        if len(items_on_correct_line) < 2:
            return inversed_tiles
        correct_line_items_index = []
        for item in line:
            if item in items_on_correct_line:
                correct_line_items_index.append(goal_line.index(item))
        for index, item in enumerate(correct_line_items_index[:-1]):
            if item > correct_line_items_index[index + 1]:
                inversed_tiles += 1
        return inversed_tiles


if __name__ == "__main__":
    initial_state = [1, 13, 11, 15, 14, 8, 9, 2, 7, 3, 0, 5, 6, 12, 4, 10]
    puzzle_size = int(math.sqrt(len(initial_state)))
    algo_info = {
        "heuristic": "improved_manhattan",
        "search_algo": "a_star",
        "goal_kind": "snail",
        "verbose": False,
        "error": '',
        "depth_limit": None,
        "time_complexity": 1,
        "space_complexity": 1,
        "start_time": None,
        "board_size": 0,
        "show_time": True,
        "show_visu": False,
        "visu_mode": False
    }
    p_goal = utils.create_goal(puzzle_size)
    initial_node = Node(None, None, initial_state, size=puzzle_size, heuristic_kind=algo_info['heuristic'], goal=p_goal)
    print(initial_node.__str__())
    node_1 = Node(initial_node, 9)
    print(node_1.__str__())
    new_node = Node(node_1, 8)
    print(new_node.__str__())
    new_node = Node(new_node, 3)
    print(new_node.__str__())
    new_node = Node(new_node, 9)
    print(new_node.__str__())
    new_node = Node(new_node, 4)
    print(new_node.__str__())
    new_node = Node(new_node, 10)
    print(new_node.__str__())
    new_node = Node(new_node, 5)
    print(new_node.__str__())
    new_node = Node(new_node, 4)
    print(new_node.__str__())
    new_node = Node(new_node, 9)
    print(new_node.__str__())
    new_node = Node(new_node, 7)
    print(new_node.__str__())

    print("\n________________________")
    node_2 = Node(initial_node, 4)
    print(node_2.__str__())
    new_node = Node(node_2, 10)
    print(new_node.__str__())
    new_node = Node(new_node, 5)
    print(new_node.__str__())
    new_node = Node(new_node, 4)
    print(new_node.__str__())
    new_node = Node(new_node, 9)
    print(new_node.__str__())
    new_node = Node(new_node, 8)
    print(new_node.__str__())
    new_node = Node(new_node, 3)
    print(new_node.__str__())
    new_node = Node(new_node, 7)
    print(new_node.__str__())
