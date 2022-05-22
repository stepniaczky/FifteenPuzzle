from queue import PriorityQueue
from time import time_ns
from solvers.strategy import Strategy
from model.board import Board


# A* search
class ASTR(Strategy):

    def solve(self, board: Board):
        node = board
        timer = time_ns()  # starting timer
        expanded = [hash(board)]

        queue = PriorityQueue()
        queue.put((0, board))

        while queue:
            node = queue.get()[1]
            self.processed += 1

            if node.is_solved():
                break

            expanded.append(hash(node))

            neighbors = self.get_neighbourhood(node)
            new_nodes = []
            for neighbour in neighbors:
                if hash(neighbour) not in expanded:
                    new_nodes.append(neighbour)
                    neighbour.path_taken = node.steps + 1
                    self.visited += 1

            if len(new_nodes) == 0:
                node = None
                break

            for new_node in new_nodes:
                h = new_node.get_dist(self.parameter) + new_node.steps
                queue.put((h, new_node))

        # when solving process is done, saves solving time
        self.elapsed_time = (time_ns() - timer) / (10 ** 6)  # nanoseconds to milliseconds

        if node is not None:
            s = ''
            while node.parent is not None:
                s = node.movement + s
                node = node.parent
            self.path = s
            self.path_length = len(self.path)
        else:
            self.path_length = -1  # if solving gone wrong
