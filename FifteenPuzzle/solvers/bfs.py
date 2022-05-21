from time import time_ns
from solvers.strategy import Strategy
from model.board import Board


# Breadth First Search
class BFS(Strategy):

    def solve(self, board):
        timer = time_ns()  # starting timer
        queue = [board]
        recursion_lvl = {}
        visited = [hash(board)]
        is_solved = False
        node: Board = board
        # self.set_rec_dict(recursion_lvl, hash(board))
        recursion_lvl[hash(board)] = 0

        while queue:
            node = queue.pop(0)
            self.processed += 1

            lvl = recursion_lvl[hash(node)]
            self.max_recursion_reached = max(lvl, self.max_recursion_reached)
            if lvl > self.MAX_RECURSION:
                break

            if node.is_solved():
                is_solved = True
                break

            for neighbour in self.get_neighbourhood(node):
                if hash(neighbour) not in visited:
                    queue.append(neighbour)
                    visited.append(hash(neighbour))
                    # self.set_rec_dict(recursion_lvl, hash(neighbour))
                    recursion_lvl[hash(neighbour)] = lvl + 1

        # when solving process is done, saves solving time
        self.elapsed_time = (time_ns() - timer) / (10 ** 6)  # nanoseconds to milliseconds
        self.visited = len(visited)
        if is_solved is True:
            s = ''
            while node.parent is not None:
                s = node.movement + s
                node = node.parent
            self.path = s
            self.path_length = len(self.path)
        else:
            self.path_length = -1
