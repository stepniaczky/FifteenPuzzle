from time import time_ns
from solvers.strategy import Strategy
from model.board import Board


# Breadth First Search
class BFS(Strategy):

    def solve(self, board):
        timer = time_ns()  # starting timer
        queue = [board]
        recursion_lvl = {}
        visited = [str(board.board)]
        is_solved = False
        end_node: Board = board
        self.set_rec_dict(recursion_lvl, board.__hash__())

        while queue:
            node = queue.pop(0)
            self.processed += 1

            position = node.__hash__()
            if recursion_lvl[position] > self.MAX_RECURSION:
                break

            if node.is_solved():
                end_node = node
                is_solved = True
                break

            for neighbour in self.get_neighbourhood(node):
                if str(neighbour.board) not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
                    self.set_rec_dict(recursion_lvl, neighbour.__hash__())

        # when solving process is done, saves solving time
        self.elapsed_time = (time_ns() - timer) / (10 ** 6)  # nanoseconds to milliseconds
        self.visited = len(visited)
        if is_solved is True:
            s = ''
            while end_node.parent is not None:
                s = end_node.movement + s
                end_node = end_node.parent
            self.path = s
            self.path_length = len(self.path)
        else:
            self.path_length = -1
