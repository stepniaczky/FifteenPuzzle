import sqlite3
from time import time_ns
from solvers.strategy import Strategy
from model.board import Board


# A* search
class ASTR(Strategy):

    def solve(self, board: Board):
        timer = time_ns()  # starting timer
        node: Board = board
        visited = [hash(board)]
        queue = [(0, board)]

        while queue:
            (h, node) = queue.pop()
            self.processed += 1

            if node.is_solved():
                break

            neighbors = self.get_neighbourhood(node)
            new_nodes = []
            for neighbour in neighbors:
                if hash(neighbour) not in visited:
                    visited.append(hash(neighbour))
                    new_nodes.append(neighbour)

            if len(new_nodes) == 0:
                break

            nearest_node = sorted(new_nodes, key=lambda x: x.get_dist(self.parameter))[0]
            h = node.get_dist(self.parameter) + h
            queue.append((h, nearest_node))

        # when solving process is done, saves solving time
        self.elapsed_time = (time_ns() - timer) / (10 ** 6)  # nanoseconds to milliseconds
        self.visited = len(visited)

        if queue is not None:
            s = ''
            while node.parent is not None:
                s = node.movement + s
                node = node.parent
            self.path = s
            self.path_length = len(self.path)
        else:
            self.path_length = -1  # if solving gone wrong