import node
import utils
import visu

size = 3
goal = utils.create_goal(size)


def algo(initial_node, mode, verbose=False) -> None:
    """
    Algorithm pre-treatment to check if initial state has a solution and redirect to the relevant function
    depending on the mode.
    :param Node initial_node: Problem node with initial conditions.
    :param str mode: Mode of algorithm. Has to be in ["a_star", "greedy", "uniform_cost", "ida_star"]
    :param bool verbose: verbose mode will print more information during search
    :return: None
    """
    if mode not in ['a_star', 'greedy', 'uniform_cost', 'ida_star']:
        return finished(None, 0, 0, error=True)
    if utils.puzzle_has_snail_solution(initial_node.state) is False:
        return finished(None, 0, 0, verbose=verbose)
    if initial_node.finished is True:
        return finished(initial_node, time_complexity, space_complexity, verbose=verbose, mode=mode)
    if mode == 'ida_star':
        return search_ida_star(initial_node, verbose=verbose)
    else:
        return search_algo(initial_node, mode, verbose=verbose)


def search_algo(initial_node, mode, verbose=False) -> None:
    """
    Algorithm for A*, greedy search or uniform_cost search to find solution to problem node.
    :param Node initial_node: Problem node with initial conditions.
    :param str mode: Mode of algorithm. Has to be in ["a_star", "greedy", "uniform_cost"]
    :param bool verbose: verbose mode will print more information during search
    :return: None
    """
    time_complexity, space_complexity = 1, 1
    nodes_queue = [initial_node]
    explored_states = {(tuple(initial_node.state),)}
    while nodes_queue:
        best_node = nodes_queue[0]
        for action in best_node.possible_actions:
            state = utils.action(best_node.state, action)
            if tuple(state) not in explored_states:
                new_node = node.Node(best_node, action, state)
                time_complexity += 1
                nodes_queue.append(new_node)
                explored_states.add(tuple(new_node.state))
                space_complexity = max(space_complexity, len(explored_states))
                if verbose:
                    verbose_print(time_complexity, space_complexity, nodes_queue, new_node)
                if new_node.finished is True:
                    return finished(new_node, time_complexity, space_complexity, verbose=verbose, mode=mode)
        nodes_queue.remove(best_node)
        nodes_queue = sort_queue(nodes_queue, mode)
    return finished(None, 0, 0, verbose=verbose)


def search_ida_star(initial_node, limit=None, time_complexity=1, space_complexity=1, verbose=False) -> None:
    """
    IDA* algorithm.
    :param Node initial_node: Problem node with initial conditions.
    :param int limit: Depth limit of this iteration of IDA
    :param int time_complexity: Time complexity when the iteration starts
    :param int space_complexity: Space complexity when the iteration starts
    :param bool verbose: verbose mode will print more information during search
    :return: None
    """
    nodes_queue = [initial_node]
    explored_states = {(tuple(initial_node.state),)}
    if limit is None:
        limit = initial_node.evaluation
    new_limit = None
    while nodes_queue:
        best_node = nodes_queue[0]
        for action in best_node.possible_actions:
            time_complexity += 1
            new_node = node.Node(best_node, action)
            if new_node.evaluation <= limit:
                nodes_queue.insert(0, new_node)
                explored_states.add(tuple(new_node.state))
                space_complexity = max(space_complexity, len(explored_states))
                if verbose:
                    verbose_print(time_complexity, space_complexity, nodes_queue, new_node)
                if new_node.finished is True:
                    return finished(new_node, time_complexity, space_complexity, verbose=verbose, mode='ida_star')
            else:
                new_limit = new_node.evaluation if new_limit is None else min(new_limit, new_node.evaluation)
        nodes_queue.remove(best_node)
    if new_limit is not None:
        search_ida_star(initial_node, new_limit, time_complexity, space_complexity)
    else:
        return finished(None, 0, 0, verbose=verbose)


def sort_queue(queue, mode) -> list:
    """
    Queue is sorted according to mode
    :param list queue:
    :param str mode:
    :return list sorted_queue:
    """
    sorted_queue = None
    if mode == "a_star":
        sorted_queue = sorted(queue, key=lambda x: x.evaluation)
    elif mode == "greedy":
        sorted_queue = sorted(queue, key=lambda x: x.heuristic)
    elif mode == "uniform_cost":
        sorted_queue = sorted(queue, key=lambda x: x.cost)
    return sorted_queue


def verbose_print(time_complexity, space_complexity, sorted_queue, new_node) -> None:
    """
    Print information during the search.
    :param int time_complexity:
    :param int space_complexity:
    :param list sorted_queue:
    :param Node new_node:
    :return None:
    """
    if time_complexity % 10000 == 0:
        print("time complexity = {}, space complexity = {}, queue = {}".format(
            time_complexity, space_complexity, len(sorted_queue)))
        print(utils.puzzle_formatted_str(new_node.state))


def finished(finish_node, time_complexity, space_complexity, error=False, verbose=False, mode=None) -> None:
    """
    Function that print solution when found.
    :param Node finish_node: Solution leaf.
    :param int time_complexity: number of nodes that have been created.
    :param int space_complexity: max concurential nodes in memory.
    :param bool error: if there is an error in the parameters given to search algo.
    :param bool verbose: verbose mode will print more information during search
    :param str mode: search algorithm mode
    :return: None
    """
    if error is True:
        print("The mode must be in ['a_star', 'greedy', 'uniform_cost', 'ida_star']")
    elif finish_node is None:
        print("This problem has no solution.")
    else:
        print(utils.puzzle_formatted_str(finish_node.state))
        solution_list = [finish_node]
        while finish_node.parent:
            finish_node = finish_node.parent
            solution_list.insert(0, finish_node)

        print("""
        This problem can be solved in {} steps.
        The time_complexity is {} and space_complexity is {}
        The steps to solve it are the following {}""".format(
            len(solution_list) - 1, time_complexity, space_complexity, [item.moved_tile for item in solution_list[1:]]))

        if verbose:
            for item in solution_list:
                print(utils.puzzle_formatted_str(item.state))

        info = utils.make_info(size, solution_list, mode, time_complexity, space_complexity)
        visu.visualization(info, 'fight')
        # if not fight show just solution


if __name__ == "__main__":
    init_state = [1, 2, 8, 3, 4, 7, 5, 6, 0]
    # size = 5
    init_state = [i for i in range(size ** 2)]
    tmp = init_state[size]
    init_state[size] = init_state[size + 1]
    init_state[size + 1] = tmp
    init_state = [4, 6, 5, 0, 2, 1, 7, 8, 3] # 25 etapes?
    # init_state = [1, 3, 2, 0]
    # init_state = [1, 2, 0, 3]
    print(utils.puzzle_formatted_str(init_state))
    init_node = node.Node(None, None, init_state)
    # initial_node = node.Node(None, None, utils.create_goal(3), utils.create_goal(3))
    # print(initial_node.__str__())
    # search_algo(init_node, mode="a_star", verbose=True)
    algo(init_node, mode="a_star", verbose=False)
    init_node = node.Node(None, None, init_state)
    algo(init_node, mode="ida_star", verbose=False)
    # search_algo(init_node, mode="uniform_cost")
