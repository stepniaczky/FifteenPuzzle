from abc import ABC, abstractmethod


class Strategy(ABC):
    MAX_RECURSION = 20

    def __init__(self):
        self.path_length = 0
        self.path = ''
        self.visited = 0
        self.processed = 0
        self.max_recursion_reached = 0
        self.elapsed_time = 0

    def get_result(self) -> list:
        return [self.path_length, self.path]

    def get_info(self) -> list:
        return [self.path_length, self.visited, self.processed,
                self.max_recursion_reached, round(self.elapsed_time, 3)]

    @abstractmethod
    def solve(self):
        pass


class DFS(Strategy):

    def solve(self):
        pass


class BFS(Strategy):

    def solve(self):
        pass


class ASTR(Strategy):

    def solve(self):
        pass
