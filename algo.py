import node
import utils


def a_star(initial_node):
    created_nodes = 1
    nodes_queue = [initial_node]
    explored_states = [initial_node.state]
    if initial_node.finished is True:
        return finished(initial_node, created_nodes)
    while nodes_queue:
        best_node = min(nodes_queue, key=lambda x: x.evaluation)  # selection du best node
        for action in best_node.possible_actions:
            new_node = node.Node(best_node, action)
            created_nodes += 1
            if created_nodes % 10000 == 0:
                print(created_nodes, len(explored_states), len(nodes_queue))
            if new_node.finished is True:
                return finished(new_node, created_nodes)
            if new_node.state not in explored_states:
                nodes_queue.append(new_node)
                explored_states.append(new_node.state)
        nodes_queue.remove(best_node)
    print("no Solutions, {} nodes created, {} states explored, {} in queue".format(created_nodes, len(explored_states),
                                                                                   len(nodes_queue)))


def finished(finish_node, created_nodes):
    print(finish_node.__str__())
    i = 0
    while finish_node.parent:
        finish_node = finish_node.parent
        print(finish_node.__str__())
        i += 1
    print("{} steps and {} created_nodes".format(i, created_nodes))


if __name__ == "__main__":
    init_state = [5, 2, 3, 8, 4, 7, 6, 1, 0]
    # init_state = [1, 3, 2, 0]
    print(utils.puzzle_formatted_str(init_state))
    init_node = node.Node(None, None, init_state)
    # initial_node = node.Node(None, None, utils.create_goal(3), utils.create_goal(3))
    # print(initial_node.__str__())
    a_star(init_node)
