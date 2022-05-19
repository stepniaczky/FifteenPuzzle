from abc import ABC, abstractmethod
from time import time_ns
from board import Board


class Strategy(ABC):
    MAX_RECURSION = 20

    def __init__(self, parameter):
        self.parameter = parameter
        self.path_length = 0
        self.path = ''
        self.visited = 0
        self.processed = 0
        self.max_recursion_reached = 0
        self.elapsed_time = 0

    # returns data required in the result file
    def get_result(self) -> list:
        if self.path_length >= 0:
            return [self.path_length, self.path]
        else:
            return [self.path_length]

    # returns data required in the additional info file
    def get_info(self) -> list:
        return [self.path_length, self.visited, self.processed,
                self.max_recursion_reached, round(self.elapsed_time, 3)]

    @abstractmethod
    def solve(self, board):
        pass

    # @staticmethod
    # def prevent_going_backward(last_move: str) -> str:
    #     if last_move == '':
    #         return ''
    #     all_moves = ['U', 'R', 'D', 'L']
    #     i = all_moves.index(last_move)
    #     if i < 2:
    #         return all_moves[i + 2]
    #     else:
    #         return all_moves[i - 2]

    # returns neighbourhood of actual empty cell position
    def get_neighbourhood(self, parent: Board) -> list:
        neighbourhood = []
        search_order = list(self.parameter)

        for direction in search_order:
            b = parent.move(direction)
            if b is not False:
                b.parent = parent
                b.movement = direction
                neighbourhood.append(b)

        return neighbourhood

    # if actual board state exists in given directory, adds 1 to its frequency
    # else adds actual board state to given directory with initial value of 1
    def set_rec_dict(self, recursion_lvl: dict, position: str):
        if position in recursion_lvl.keys():
            recursion_lvl[position] += 1
        else:
            recursion_lvl[position] = 1
        self.max_recursion_reached = max(recursion_lvl[position], self.max_recursion_reached)


class DFS(Strategy):

    def solve(self, board):
        pass


class BFS(Strategy):

    def solve(self, board):
        timer = time_ns()
        queue = [board]
        recursion_lvl = {}
        visited = []
        is_solved = False
        end_node: Board = board
        self.set_rec_dict(recursion_lvl, str(board.board))

        while queue:
            node = queue.pop(0)
            self.processed += 1

            position = str(node.board)
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
                    self.set_rec_dict(recursion_lvl, str(neighbour.board))

        # when solving process is done
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


class ASTR(Strategy):

    def solve(self, board):
        pass
