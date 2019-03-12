import math
import copy


# size


def fill_right(n, sorted_list, x, y, i):
    """
    Fill the number from left to right until it reaches the border or an already filled slot, update i, x, y values"
    :param int n: size of puzzle
    :param list sorted_list: list with the position of each value in the good spot
    :param int i: current value to be added int the list
    :param int x: x coordinate in the puzzle
    :param int y: y coordinate in the puzzle
    :return list: list of size n^2 with the solution
    """

    if sorted_list[(n * y) + x] != 0:
        x += 1

    while x < n - 1 and sorted_list[(n * y) + x] == 0 and i < n ** 2:
        sorted_list[(n * y) + x] = i
        i += 1
        if sorted_list[(n * y) + x + 1] == 0:
            x += 1
    return sorted_list, x, y, i


def fill_down(n, sorted_list, x, y, i):
    """
    Fill the number from up to down until it reaches the border or an already filled slot, update i, x, y values"
    :param int n: size of puzzle
    :param list sorted_list: list with the position of each value in the good spot
    :param int i: current value to be added int the list
    :param int x: x coordinate in the puzzle
    :param int y: y coordinate in the puzzle
    :return list: list of size n^2 with the solution
    """

    if sorted_list[(n * y) + x] != 0:
        y += 1

    while y < n - 1 and sorted_list[(n * y) + x] == 0 and i < n ** 2:
        sorted_list[(n * y) + x] = i
        i += 1
        if sorted_list[(n * (y + 1)) + x] == 0:
            y += 1
    return sorted_list, x, y, i


def fill_left(n, sorted_list, x, y, i):
    """
    Fill the number from right to left until it reaches the border or an already filled slot, update i, x, y values"
    :param int n: size of puzzle
    :param list sorted_list: list with the position of each value in the good spot
    :param int i: current value to be added int the list
    :param int x: x coordinate in the puzzle
    :param int y: y coordinate in the puzzle
    :return list: list of size n^2 with the solution
    """
    if sorted_list[(n * y) + x] != 0 and x > 0:
        x -= 1

    while x >= 0 and sorted_list[(n * y) + x] == 0 and i < n ** 2:
        sorted_list[(n * y) + x] = i
        i += 1
        if x > 0 and sorted_list[(n * y) + x - 1] == 0:
            x -= 1
    return sorted_list, x, y, i


def fill_up(n, sorted_list, x, y, i):
    """
    Fill the number from down to up until it reaches the border or an already filled slot, update i, x, y values"
    :param int n: size of puzzle
    :param list sorted_list: list with the position of each value in the good spot
    :param int i: current value to be added int the list
    :param int x: x coordinate in the puzzle
    :param int y: y coordinate in the puzzle
    :return list: list of size n^2 with the solution
    """
    if sorted_list[(n * y) + x] != 0:
        y -= 1

    while y > 0 and sorted_list[(n * y) + x] == 0 and i < n ** 2:
        sorted_list[(n * y) + x] = i
        i += 1
        if y > 1 and sorted_list[(n * (y - 1)) + x] == 0:
            y -= 1
    return sorted_list, x, y, i


def create_goal(n) -> list:
    """
    Returns as a list the goal to reach for a n-puzzle of size n in a snail style"
    :param int n: size of puzzle
    :return list: list of size n^2 with the solution
    """

    sorted_list = [0] * (n ** 2)
    i = 1
    x, y = 0, 0

    while i < n ** 2:
        if i < n ** 2:
            sorted_list, x, y, i = fill_right(n, sorted_list, x, y, i)
        if i < n ** 2:
            sorted_list, x, y, i = fill_down(n, sorted_list, x, y, i)
        if i < n ** 2:
            sorted_list, x, y, i = fill_left(n, sorted_list, x, y, i)
        if i < n ** 2:
            sorted_list, x, y, i = fill_up(n, sorted_list, x, y, i)

    return sorted_list


def action(puzzle, tile) -> list:
    """
    Returns the state of the puzzle after swapping tile. Returns error if tile can not be swapped.
    :param list puzzle:
    :param int tile:
    :return list:
    """

    try:
        index_zero, index_tile = 0, 0
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

        vertical_swap = (x_tile == x_zero and abs(y_tile - y_zero) == 1)
        horizontal_swap = (y_tile == y_zero and abs(x_tile - x_zero) == 1)
        if not (horizontal_swap or vertical_swap):
            raise Exception("No swap possible")

        new_state_puzzle = copy.deepcopy(puzzle)
        new_state_puzzle[int(y_tile * size + x_tile)] = 0
        new_state_puzzle[int(y_zero * size + x_zero)] = tile
        return new_state_puzzle
    except Exception("No swap possible") as e:
        print(e)

    # should probably create class Tile with value, index, x, y


def puzzle_formatted_str(puzzle) -> None:
    """

    :param list puzzle:
    :return: void function
    """
    length = len(puzzle)
    size = int(math.sqrt(length))
    padding = 0
    while length // 10 > 0:
        length //= 10
        padding += 1
    padding += 1

    string = ""
    for y in range(size):
        for x in range(size):
            if x < size - 1:
                string += "{:{}}, ".format(puzzle[y * size + x], padding)
            elif y < size - 1:
                string += "{:{}}\n".format(puzzle[y * size + x], padding)
            else:
                string += "{:{}}\n\n".format(puzzle[y * size + x], padding)
    return string


def puzzle_has_snail_solution(puzzle):
    """
    Check if a snail solution is possible.
    :param list puzzle: n_puzzle state
    :return: boolean
    """
    n = 0
    for index, tile in enumerate(puzzle[:-1]):
        for sub_index, following_tile in enumerate(puzzle[index + 1:]):
            if tile > following_tile > 0:
                n += 1
    print(n)
    return n % 2 == 1


if __name__ == "__main__":
    P = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    puzzle_has_snail_solution(P)
    P = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    puzzle_has_snail_solution(P)
    P = [0, 2, 1, 3, 4, 5, 6, 7, 8]
    puzzle_has_snail_solution(P)
    P = [5, 2, 3, 8, 4, 7, 1, 6, 0]
    puzzle_has_snail_solution(P)
    print(puzzle_formatted_str(P))
    # Q = action(P, 1)
    # print(puzzle_formatted_str(Q))
    # print_puzzle_puzzle(Q)
    # Q = action(P, 2)
    # print_puzzle(Q)
    # Q = action(P, 3)
    # print_puzzle(Q)
    # Q = action(P, 4)
    # print_puzzle(Q)
    # Q = action(P, 5)
    # print_puzzle(Q)
    # Q = action(P, 6)
    # print_puzzle(Q)
    # Q = action(P, 7)
    # print_puzzle(Q)
    # Q = action(P, 8)
    # print_puzzle(Q)

    # P = create_goal(3)
    # puzzle_formatted_str(P)
    # P = create_goal(4)
    # puzzle_formatted_str(P)
    # P = create_goal(5)
    # puzzle_formatted_str(P)
    # P = create_goal(10)
    # print_puzzle(P)
    # P = create_goal(30)
    # print_puzzle(P)
