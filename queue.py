class Queue:
    def __init__(self, initial_node=None, mode='a_star'):
        self.priority_queue = [initial_node]
        self.mode = mode

    def insert_node(self, new_node) -> None:

        self.priority_queue.insert(0, new_node)
        if self.mode == "a_star":
            self.priority_queue.sort(key=lambda x: x.evaluation)
        elif self.mode == "greedy":
            self.priority_queue.sort(key=lambda x: x.heuristic)
        elif self.mode == "uniform_cost":
            self.priority_queue.sort(key=lambda x: x.cost)
