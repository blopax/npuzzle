import argparse
import parser
import algo
import node
import utils
import os



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, required= True,
                        help="Name of the file containing the npuzzle. File must be absolute path.\n")
    parser.add_argument("-s", "--heuristic", type=str, default="improved_manhattan",
                        choices=["manhattan", "misplaced", "improved_manhattan"],
                        help="Choose the heuristic to be used.\n")
    parser.add_argument("-a", "--algorithm", type=str, default="a_star",
                        choices=["a_star", "ida_star", "greedy", "uniform_cost"],
                        help="Choose the algorithm to be used.\n")
    parser.add_argument("-v", "--verbosity", action="store_true", help="Toggle verbose mode.\n")
    parser.add_argument("-t", "--time", action="store_true", help="Show the time needed to resolve the npuzzle.\n")
    parser.add_argument("-visu", "--visual", action="store_true", help="Toggle Visual mode.\n")
    parser.add_argument("-visumode", "--visual_mode", type=str, default="fight", choices={"fight", "solution"},
                        help="Define the type of visual.\n")
    parser.add_argument("-p", "--puzzle", type=str, default="snail", choices={"snail", "classic"},
                        help="Choose which kind of puzzle you would like to solve.\n")

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    algo_info = utils.create_info_algo(args)
    if os.path.isfile(args.file):
        parser.check_file(algo_info, args.file)
    else:
        algo_info["error"] = "{0} is not a valid file".format(args.file)
    if algo_info["error"] == '':
        algo_info["goal"] = utils.create_goal(algo_info["board_size"], algo_info["goal_kind"])
        init_node = node.Node(None, None, algo_info["puzzle"], algo_info["heuristic"], algo_info["board_size"], algo_info["goal"])
        algo.algo(init_node, algo_info)
    else:
        print(algo_info["error"])
