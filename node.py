import utils


class Node:
    def __init__(self, parent=None, moved_tile=None, state=None, goal=None):
        self.parent = parent
        self.moved_tile = moved_tile
        if parent is None:
            self.cost = 0
            self.state = state
        else:
            self.cost = self.parent.cost + 1
            self.state = utils.action(parent, moved_tile)
        if goal is None:
            self.goal = parent.goal
        else:
            self.goal = goal
        self.evaluation = self.cost + self.heuristic(self.state, goal)


if __name__ == "__main__":
    inital_node = Node([0, 1, 2, 3, 4, 5, 6, 7, 8], None, None, utils.create_goal(3))
