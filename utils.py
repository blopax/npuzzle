import math
import copy


def create_info_algo(args) -> dict:
    """
    Fill the info_algo dico needed for the program based on the arguments parsed"
    :param args
    :return dict: dict containing all the information needed to run the algorithm in the program
    """
    return {
        "heuristic": args.heuristic,
        "search_algo": args.algorithm,
        "goal_kind": args.puzzle,
        "verbose": args.verbosity,
        "error": '',
        "depth_limit": None,
        "time_complexity": 1,
        "space_complexity": 1,
        "start_time": None,
        "board_size": 0,
        "show_time": args.time,
        "show_visu": args.visual,
        "visu_mode": args.visual_mode
    }


def fill_right(n, sorted_list, x, y, i) -> (list, int, int, int):
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


def fill_down(n, sorted_list, x, y, i) -> (list, int, int, int):
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


def fill_left(n, sorted_list, x, y, i) -> (list, int, int, int):
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


def fill_up(n, sorted_list, x, y, i) -> (list, int, int, int):
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


def create_goal(n, goal_kind='snail') -> list:
    """
    Returns as a list the goal to reach for a n-puzzle of size n in a snail style"
    :param int n: size of puzzle
    :param str goal_kind: define what is the goal snail or classic
    :return list: list of size n^2 with the solution
    """

    if goal_kind != 'snail':
        return [i for i in range(n ** 2)]
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
        if tile not in puzzle:
            raise Exception("No swap possible")
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


def puzzle_formatted_str(puzzle) -> str:
    """
    Transforms list puzzle to a formatted string that can be printed with nice padding.
    :param list puzzle: Puzzle as a list
    :return str string: Puzzle as a formatted string
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


def puzzle_has_solution(puzzle, goal_kind='snail') -> bool:
    """
    Check if snail has no solution.
    :param list puzzle: n_puzzle state
    :param str goal_kind: define what is the goal snail or classic
    :return: boolean
    """
    goal_parity = int(goal_kind == 'snail')
    n = 0
    for index, tile in enumerate(puzzle[:-1]):
        for sub_index, following_tile in enumerate(puzzle[index + 1:]):
            if tile > following_tile > 0:
                n += 1

    size = int(math.sqrt(len(puzzle)))
    if size % 2 == 0:
        zero_index = puzzle.index(0)
        zero_row = zero_index / size
        return (n + zero_row) % 2 == goal_parity
    else:
        return n % 2 == goal_parity


if __name__ == "__main__":
    P = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    puzzle_has_solution(P)
    print(puzzle_formatted_str(P))
