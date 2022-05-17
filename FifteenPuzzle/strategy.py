from abc import ABC, abstractmethod


class Strategy(ABC):

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
