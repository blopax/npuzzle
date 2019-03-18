import argparse
import parser


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default=False,
                        help="Name of the file containing the npuzzle. File must be absolute path")
    parser.add_argument("-he", "--heuristic", type=str, default="manhattan",
                        choices=["manhattan", "misplaced", "distance"],
                        help="Choose the heuristic to be used")
    parser.add_argument("-a", "--algorithm", type=str, default="a_star",
                        choices=["a_star", "ida_star", "greedy", "uniform_cost"],
                        help="Choose the algorithm to be used")
    parser.add_argument("-v", "--verbosity", type=int, default=0, choices=[0, 1, 2, 3],
                        help="Verbose mode")
    #parser.add_argument("-o", "--output", type=str, default=sys.stdout,
    #                    help="Name of the file where you want to print the output. By default standard output")
    parser.add_argument("-visu", "--visual", type=str, default=False, choices={False, True},
                        help="Toggle Visual mode")
    parser.add_argument("-p", "--puzzle", type=str, default="snail", choices={"snail", "classic"},
                        help="Choose which kind of puzzle you would like to solve.")
    
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    error = ''
    if args.file is not False:
        error = parser.check_file(error, args.file)
        print(error)


# parser add relevant info and feed info dictionary (where +, maybe create util functions with default)
# + create initial Node


# algo_info = {
#     +  'heuristic': 'improved_manhattan',
#     +  'search_algo': 'ida_star',
#     'allowed_search_algos': ['a_star', 'greedy', 'uniform_cost', 'ida_star'],
#     +  'goal_kind': 'snail',
#     +  'verbose': False,
#     'error': False,
#     'depth_limit': None,
#     'time_complexity': 1,
#     'space_complexity': 1,
#     'start_time': None,
#     +   'board_size': size,
#     +   'show_time': True,
#     +   'show_visu': True,
#     +   'visu_mode': 'fight',
# }