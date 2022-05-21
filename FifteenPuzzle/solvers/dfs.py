from solvers.strategy import Strategy
from time import time_ns
from model.board import Board


# Depth First Search
class DFS(Strategy):

    def __init__(self, parameter):
        super().__init__(parameter)
        self.visited_list = []
        self.break_flag = False

    def solve(self, board):
        timer = time_ns()  # starting timer
        self.visited_list.append(hash(board))
        end_node: Board = self.__dfs(board, 1)

        # when solving process is done, saves solving time
        self.elapsed_time = (time_ns() - timer) / (10 ** 6)  # nanoseconds to milliseconds
        self.visited = len(self.visited_list)
        if self.break_flag is False:
            s = ''
            while end_node.parent is not None:
                s = end_node.movement + s
                end_node = end_node.parent
            self.path = s
            self.path_length = len(self.path)
        else:
            self.path_length = -1

    def __dfs(self, node: Board, rec_lvl: int):
        if self.break_flag is True:
            return None

        if node in self.visited_list:
            return None
        else:
            self.visited_list.append(hash(node))

        if node.is_solved():
            return node

        self.recursion = max(self.max_recursion_reached, rec_lvl)
        if rec_lvl > self.MAX_RECURSION:
            self.break_flag = True
            return None

        for neighbour in self.get_neighbourhood(node):
            self.processed += 1
            neighbour_board = self.__dfs(neighbour, rec_lvl + 1)
            if neighbour_board is not None:
                return neighbour_board
