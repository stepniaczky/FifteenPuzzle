from solvers.strategy import Strategy
from time import time_ns
from model.board import Board


# Depth First Search
class DFS(Strategy):

    def __init__(self, parameter: str):
        super().__init__(parameter)
        self.expanded = {}
        self.break_flag = False
        self._dict = {}

    def solve(self, board: Board):
        timer = time_ns()
        end_node = self.__dfs(board, 1)
        self.elapsed_time = (time_ns() - timer) / (10 ** 6)  # nanoseconds to milliseconds

        if end_node is None:
            self.path_length = -1
        else:
            s = ''
            while end_node.parent is not None:
                s = end_node.movement + s
                end_node = end_node.parent
            self.path = s
            self.path_length = len(self.path)

    def __dfs(self, node: Board, recursion_lvl: int) -> Board:

        self.max_recursion_reached = max(self.max_recursion_reached, recursion_lvl)
        if recursion_lvl > self.MAX_RECURSION:
            return None

        if node.is_solved():
            return node

        if hash(node) not in self.expanded:
            self.expanded[hash(node)] = node.steps
            neighbors = self.get_neighbourhood(node)
            for neighbour in neighbors:
                if hash(neighbour) in self.expanded.keys():
                    continue
                self.visited += 1
                self.processed += 1
                child_board = self.__dfs(neighbour, recursion_lvl + 1)
                if child_board is not None:
                    return child_board
