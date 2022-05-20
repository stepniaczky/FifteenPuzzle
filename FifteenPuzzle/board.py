import copy


class Board:

    def __init__(self, initial: list):
        self.initial_list = initial
        self.r, self.c = list(map(int, initial[0].split()))  # number of rows and columns
        self.SIZE = self.r * self.c  # number of elements in board
        self.board = [list(map(int, row.split())) for row in initial[1:]]  # board list with integer values
        self.check_dimensions()
        self.check_elements()
        self.parent = None  # board state before last movement
        self.movement = ''  # the direction to move parent board to current state

    # checks if every row and column of the given initial board has the same length
    # as integers written in the first line of the initial board file [rows columns]
    def check_dimensions(self):
        try:
            for i, row in enumerate(self.board):
                assert len(row) == self.c, 'BoardError: Given number of board columns is incorrect!'
                assert i < self.r, 'BoardError: Given number of board rows is incorrect!'
        # quit program with appropriate message if board dimensions are incorrect
        except AssertionError as msg:
            quit(msg)

    # checks if every element of board is in range [0, 15]
    # checks if board has not duplicates elements
    def check_elements(self):
        # dictionary in which keys stands for all elements that should exist in proper board
        # and values stands for frequency of each element in test initial board (checking for duplicates)
        correct_values = {}
        for i in range(self.SIZE):
            correct_values[i] = 0

        try:
            for row in self.board:
                for col in row:
                    assert col in correct_values.keys(), \
                        'BoardError: Value of the board element is out of range [0, 15]!'
                    correct_values[col] += 1
                    assert correct_values[col] <= 1, 'BoardError: Board has duplicate element values!'
        except AssertionError as msg:
            quit(msg)

    # checks if board is solved correctly, which means that board elements
    # starts with 1 then iterates one by one to 15 and the last element of board equals 0
    # returns True if board is solved, else False
    def is_solved(self) -> bool:
        try:
            for row_id, row in enumerate(self.board):
                for i, element in enumerate(row, start=(row_id * self.r + 1)):
                    if i == self.SIZE:
                        assert element == 0
                        break  # after checking all elements break and return True
                    assert element == i
            return True
        except AssertionError:
            return False

    # checks if moving empty cell in given direction is possible
    # if so it returns copy of board with appropriate shift
    # if it is not possible, method returns False
    def move(self, direction: str) -> bool or list:
        b = copy.deepcopy(self.board)
        row, col = self.get_xy(0)
        try:
            match direction:
                case 'U':
                    if row == 0:
                        return False
                    b[row][col], b[row - 1][col] = b[row - 1][col], b[row][col]
                case 'D':
                    b[row][col], b[row + 1][col] = b[row + 1][col], b[row][col]
                case 'R':
                    b[row][col], b[row][col + 1] = b[row][col + 1], b[row][col]
                case 'L':
                    if col == 0:
                        return False
                    b[row][col], b[row][col - 1] = b[row][col - 1], b[row][col]
                case _:
                    return False
            moved_board = self.__copy__()
            moved_board.board = b
            return moved_board  # if move passed correctly return copy of board with given shift
        except IndexError:
            return False

    # prints board
    def __str__(self) -> str:
        s = ''
        for row in self.board:
            for i, col in enumerate(row):
                s += f'  {col} ' if col < 10 else f' {col} '
                if (i + 1) % self.r == 0:
                    s += '\n'
        return s

    # returns string
    def __repr__(self):
        return f"Board({self.initial_list})"

    # returns deep copy of this
    def __copy__(self):
        b = eval(self.__repr__())
        b.board = self.board
        return b

    # returns row and column of given element in board
    def get_xy(self, element: int) -> tuple:
        for i, row in enumerate(self.board):
            if element in row:
                return i, row.index(element)
