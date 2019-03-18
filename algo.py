import node
import utils
import time


def algo(initial_node, info) -> None:
    """
    Algorithm pre-treatment to check if initial state has a solution and redirect to the relevant function
    depending on the mode.
    :param Node initial_node: Problem node with initial conditions.
    :param dict info: Dict with relevant info for algo
    :return: None
    """

    if utils.puzzle_has_solution(initial_node.state, info['goal_kind']) is False:
        return finished(None, info)
    if initial_node.finished is True:
        return finished(initial_node, info)
    if info['search_algo'] == 'ida_star':
        info['time'] = time.time()
        return search_ida_star(initial_node, info)
    else:
        info['time'] = time.time()
        return search_algo(initial_node, info)


def search_algo(initial_node, info) -> None:
    """
    Algorithm for A*, greedy search or uniform_cost search to find solution to problem node.
    :param Node initial_node: Problem node with initial conditions.
    :param dict info: Dict with relevant info for algo
    :return: None
    """
    nodes_queue = [initial_node]
    explored_states = {(tuple(initial_node.state),)}
    while nodes_queue:
        best_node = nodes_queue[0]
        for action in best_node.possible_actions:
            state = utils.action(best_node.state, action)
            if tuple(state) not in explored_states:
                new_node = node.Node(best_node, action, state)
                info['time_complexity'] += 1
                nodes_queue.append(new_node)
                explored_states.add(tuple(new_node.state))
                info['space_complexity'] = max(info['space_complexity'], len(explored_states))
                if info['verbose']:
                    verbose_print(info, nodes_queue, new_node)
                if new_node.finished is True:
                    return finished(new_node, info)
        nodes_queue.remove(best_node)
        nodes_queue = sort_queue(nodes_queue, info['search_algo'])
    return finished(None, info)


def search_ida_star(initial_node, info) -> None:
    """
    IDA* algorithm.
    :param Node initial_node: Problem node with initial conditions.
    :param dict info: Dict with relevant info for algo
    :return: None
    """
    nodes_queue = [initial_node]
    explored_states = {(tuple(initial_node.state),)}
    if info['depth_limit'] is None:
        info['depth_limit'] = initial_node.evaluation
    info['new_depth_limit'] = None
    while nodes_queue:
        best_node = nodes_queue[0]
        for action in best_node.possible_actions:
            info['time_complexity'] += 1
            new_node = node.Node(best_node, action)
            if new_node.evaluation <= info['depth_limit']:
                nodes_queue.insert(0, new_node)
                explored_states.add(tuple(new_node.state))
                info['space_complexity'] = max(info['space_complexity'], len(explored_states))
                if info['verbose']:
                    verbose_print(info, nodes_queue, new_node)
                if new_node.finished is True:
                    return finished(new_node, info)
            elif info['new_depth_limit'] is None:
                info['new_depth_limit'] = new_node.evaluation
            else:
                info['new_depth_limit'] = min(info['new_depth_limit'], new_node.evaluation)
        nodes_queue.remove(best_node)
    if info['new_depth_limit'] is not None:
        info['depth_limit'] = info['new_depth_limit']
        search_ida_star(initial_node, info)
    else:
        return finished(None, info)


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


def verbose_print(info, sorted_queue, new_node) -> None:
    """
    Print information during the search.
    :param dict info: Dict with relevant info for algo
    :param list sorted_queue:
    :param Node new_node:
    :return None:
    """
    if info['time_complexity'] % 10000 == 0:
        print("time complexity = {}, space complexity = {}, queue = {}".format(
            info['time_complexity'], info['space_complexity'], len(sorted_queue)))
        print(utils.puzzle_formatted_str(new_node.state))


def finished(finish_node, info) -> None:
    """
    Function that print solution when found.
    :param Node finish_node: Solution leaf.
    :param dict info: Dict with relevant info for algo
    :return: None
    """

    if finish_node is None:
        print("This problem has no solution.")
    else:
        info['time'] = round(time.time() - info['time'], 2)
        solution_list = [finish_node]
        while finish_node.parent:
            finish_node = finish_node.parent
            solution_list.insert(0, finish_node)
        print("""
This problem can be solved in {} steps.
The time_complexity is {} and space_complexity is {}
The steps to solve it are the following {}""".format(
            len(solution_list) - 1, info['time_complexity'], info['space_complexity'],
            [item.moved_tile for item in solution_list[1:]]))
        if info['show_time']:
            print('Time used: {}s'.format(info['time']))
        if info['verbose']:
            for item in solution_list:
                print(utils.puzzle_formatted_str(item.state))
        if info["show_visu"]:
            import visu
            visu.visualization(info, solution_list)


if __name__ == "__main__":
    # init_state = [1, 2, 8, 3, 4, 7, 5, 6, 0]
    # init_state = [4, 6, 5, 0, 2, 1, 7, 8, 3]  # 25 etapes?
    # init_state = [6, 4, 5, 0, 2, 1, 7, 8, 3] # classic
    init_state = [i for i in range(size ** 2)]
    # random.shuffle(init_state)
    tmp = init_state[size]
    init_state[size] = init_state[size + 1]
    init_state[size + 1] = tmp
    print(utils.puzzle_formatted_str(init_state))
    init_node = node.Node(None, None, init_state)

    algo(init_node, algo_info)
