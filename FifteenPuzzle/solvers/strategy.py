from abc import ABC, abstractmethod
from model.board import Board


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

    # returns neighbourhood of actual empty cell position
    def get_neighbourhood(self, parent: Board) -> list:
        neighbourhood = []
        search_order = list

        # if strategy equals astr, search_order variable gets random directions
        # astr algorithm is based on the distances of next nodes and completely independent of directions
        if self.parameter in ['manh', 'hamm']:
            search_order = list('URDL')
        else:
            search_order = list(self.parameter)

        # creates neighbourhood list that is based on strategy searching order
        for direction in search_order:
            b = parent.move(direction)
            if b is not False:
                b.parent = parent  # assigns parent to this node
                b.movement = direction  # assigns direction of the parent shift to get this node
                neighbourhood.append(b)

        return neighbourhood

    @abstractmethod
    def solve(self, board):
        pass
