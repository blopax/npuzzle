import sys
import argparse
import random
import utils


def make_puzzle(size, snail):
    puzzle_list = [i for i in range(size ** 2)]
    random.shuffle(puzzle_list)

    snail_goal = utils.puzzle_has_solution(puzzle_list)
    if (snail_goal and snail) or (not snail_goal and not snail):
        return puzzle_list
    else:
        if puzzle_list[0] == 0 or puzzle_list[1] == 0:
            puzzle_list[-1], puzzle_list[-2] = puzzle_list[-2], puzzle_list[-1]
        else:
            puzzle_list[0], puzzle_list[1] = puzzle_list[1], puzzle_list[0]
        return puzzle_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("size", type=int, help="Size of the puzzle's side. Must be >3.", default=3)
    parser.add_argument("-s", "--solvable", type=str, default='True',
                        help="Says if solvable or not")
    args = parser.parse_args()
    random.seed()

    if args.size < 3:
        print("Can't generate a puzzle with size lower than 2. It says so in the help. Dummy.")
        sys.exit(1)

    solvable = args.solvable == 'True'
    s = args.size
    puzzle = make_puzzle(s, solvable)

    w = len(str(s * s))
    print("# This puzzle is {}".format("solvable" if solvable else "unsolvable"))
    print("{}\n".format(s))
    for y in range(s):
        for x in range(s):
            print("{} ".format((str(puzzle[x + y * s]).rjust(w))), end='')
        print()
