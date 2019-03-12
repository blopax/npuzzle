import node
import utils


size = 3
goal = utils.create_goal(size)


def a_star(initial_node) -> None:
    """
    A* algorithm to find an optimal solution to problem node.
    :param Node initial_node: Problem node with initial conditions.
    :return: None
    """
    time_complexity = 1
    space_complexity = 1
    nodes_queue = [initial_node]
    explored_states = [initial_node.state]
    if initial_node.finished is True:
        return finished(initial_node, time_complexity, space_complexity)
    while nodes_queue:
        sorted_queue = sorted(nodes_queue, key=lambda x: x.evaluation)  # selection du best node
        best_node = sorted_queue[0]
        for action in best_node.possible_actions:
            state = utils.action(best_node.state, action)
            if state not in explored_states:
                new_node = node.Node(best_node, action, state)
                time_complexity += 1
                nodes_queue.append(new_node)
                explored_states.append(new_node.state)
                space_complexity = max(space_complexity, len(explored_states))
                if new_node.finished is True:
                    return finished(new_node, time_complexity, space_complexity)
        nodes_queue.remove(best_node)
    print("no Solutions, time complexity: {} nodes created, space complexity: {} states explored, "
          "{} in queue".format(time_complexity, space_complexity, len(nodes_queue)))


def finished(finish_node, time_complexity, space_complexity) -> None:
    """
    Function that print solution when found.
    :param Node finish_node: Solution leaf.
    :param int time_complexity: number of nodes that have been created.
    :param int space_complexity: max concurential nodes in memory.
    :return: None
    """
    print(finish_node.__str__())
    i = 0
    while finish_node.parent:
        finish_node = finish_node.parent
        print(finish_node.__str__())
        i += 1
    print("{} steps and {} time_complexity and {} space_complexity".format(i, time_complexity, space_complexity))


if __name__ == "__main__":
    init_state = [5, 2, 3, 8, 4, 7, 1, 6, 0]
    # init_state = [1, 3, 2, 0]
    print(utils.puzzle_formatted_str(init_state))
    init_node = node.Node(None, None, init_state)
    # initial_node = node.Node(None, None, utils.create_goal(3), utils.create_goal(3))
    # print(initial_node.__str__())
    a_star(init_node)