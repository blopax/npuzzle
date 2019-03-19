import sys
import argparse
import random
import utils


def make_puzzle(s, solvable):
    puzzle = [i for i in s ** 2]
    random.shuffle(puzzle)

    snail_goal = utils.puzzle_has_solution(puzzle)
    if (snail_goal and solvable) or (not snail_goal and not solvable):
        return puzzle
    else:
        if puzzle[0] == 0 or puzzle[1] == 0:
            puzzle[-1], puzzle[-2] = puzzle[-2], puzzle[-1]
        else:
            puzzle[0], puzzle[1] = puzzle[1], puzzle[0]
        return puzzle


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("size", type=int, help="Size of the puzzle's side. Must be >3.")
    parser.add_argument("-s", "--solvable", action="store_true", default=False,
                        help="Forces generation of a solvable puzzle. Overrides -u.")
    parser.add_argument("-u", "--unsolvable", action="store_true", default=False,
                        help="Forces generation of an unsolvable puzzle")
    args = parser.parse_args()
    random.seed()

    if args.solvable and args.unsolvable:
        print("Can't be both solvable AND unsolvable, dummy !")
        sys.exit(1)

    if args.size < 3:
        print("Can't generate a puzzle with size lower than 2. It says so in the help. Dummy.")
        sys.exit(1)

    puzzle = make_puzzle(s, solvable=solv)

    w = len(str(s * s))
    print("# This puzzle is {}".format("solvable" if solv else "unsolvable"))
    print("{}\n".format(s))
    for y in range(s):
        for x in range(s):
            print("{} ".format((str(puzzle[x + y * s]).rjust(w))), end='')
        print()
