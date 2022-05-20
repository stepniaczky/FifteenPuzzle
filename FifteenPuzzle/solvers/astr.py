from time import time_ns
from solvers.strategy import Strategy
from model.board import Board


class ASTR(Strategy):

    def solve(self, board):
        timer = time_ns()  # starting timer
        node: Board = board
        visited = [board.__hash__()]
        queue = [0, board]

        while queue:
            self.processed += 1

            if node.is_solved():
                break

            neighbors = self.get_neighbourhood(node)
            for neighbour in neighbors:
                if neighbour.__hash__() not in visited:
                    visited.append(neighbour.__hash__())
                else:
                    neighbors.remove(neighbour)
            else:
                queue = [-1, None]
            node = sorted(neighbors, key=lambda x: x.get_dist(self.parameter))[0]
            h = node.get_dist(self.parameter) + queue[0]
            queue = [h, node]

        # when solving process is done, saves solving time
        self.elapsed_time = (time_ns() - timer) / (10 ** 6)  # nanoseconds to milliseconds
        self.visited = len(visited)

        if queue[1] is not None:
            s = ''
            while node.parent is not None:
                s = node.movement + s
                node = node.parent
            self.path = s
            self.path_length = len(self.path)
        else:
            self.path_length = -1
