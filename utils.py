import math
import copy


def create_goal(n) ->list:
    """
    Returns as a list the goal to reach for a n-puzzle of size n in a snail style"
    :param int n: size of puzzle
    :return list: list of size n^2 with the solution
    """


def action(puzzle, tile) ->list:
    """
    Returns the state of the puzzle after swapping tile. Returns error if tile can not be swapped.
    :param list puzzle:
    :param int tile:
    :return list:
    """

    try:
        for index, item in enumerate(puzzle):
            if item == 0:
                index_zero = index
            if item == tile:
                index_tile = index

        size = math.sqrt(len(puzzle))
        x_tile = index_tile % size
        y_tile = index_tile // size
        x_zero = index_zero % size
        y_zero = index_zero // size

        vertical_swap = (x_tile == x_zero and math.fabs(y_tile - y_zero) == 1)
        horizontal_swap = (y_tile == y_zero and math.fabs(x_tile - x_zero) == 1)
        if not (horizontal_swap or vertical_swap):
            raise Exception("No swap possible")

        new_state_puzzle = copy.deepcopy(puzzle)
        new_state_puzzle[int(y_tile * size + x_tile)] = 0
        new_state_puzzle[int(y_zero * size + x_zero)] = tile
        return new_state_puzzle
    except Exception as e:
        print(e)

    #should probably create class Tile with value, index, x, y


def print_puzzle(puzzle) ->None:
    """

    :param list puzzle:
    :return: void function
    """


if __name__ == "__main__":
    P = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(P)
    Q = action(P, 1)
    print(Q)
    Q = action(P, 2)
    print(Q)
    Q = action(P, 3)
    print(Q)
    Q = action(P, 4)
    print(Q)
    Q = action(P, 5)
    print(Q)
    Q = action(P, 6)
    print(Q)
    Q = action(P, 7)
    print(Q)
    Q = action(P, 8)
    print(Q)
