class Board:

    def __init__(self, initial: list):
        self.r, self.c = initial[0].split()  # number of rows and columns
        self.board = [list(row.split()) for row in initial[1:]]  # board list
        self.check_size()
        self.SIZE = self.r * self.c  # number of elements in board

    # checks if every row and column of the given initial board has the same length
    # as integers written in the first line of the initial board file [rows columns]
    def check_size(self):
        try:
            for i, row in self.board:
                assert len(row) == self.c, 'Given number of board columns is incorrect!'
                assert i < self.r, 'Given number of board rows is incorrect!'
        # quit program with appropriate message if board dimensions are incorrect
        except AssertionError as msg:
            exit(msg)

    # checks if board is solved correctly, which means that board elements
    # starts with 1 then iterates one by one to 15 and the last element of board equals 0
    # returns True if board is solved, else False
    def is_solved(self) -> bool:
        try:
            for i, element in enumerate(self.board, start=1):
                if i == self.SIZE - 1:
                    assert element == 0
                assert element == 1
            return True
        except AssertionError:
            return False

    # returns tuple of row and column index of empty cell in board
    def get_empty_cell(self) -> tuple:
        for i, row in enumerate(self.board):
            if 0 in row:
                return i, row.index(0)

    # checks if move in given direction is possible, if so it returns copy of board with appropriate shift
    # if it is not possible, method returns False
    def move(self, direction: str) -> bool or list:
        b = self.board.copy()
        row, col = self.get_empty_cell()
        try:
            match direction:
                case 'U':
                    b[row][col], b[row - 1][col] = b[row - 1][col], b[row][col]
                case 'D':
                    b[row][col], b[row + 1][col] = b[row + 1][col], b[row][col]
                case 'R':
                    b[row][col], b[row][col - 1] = b[row][col - 1], b[row][col]
                case 'L':
                    b[row][col], b[row][col + 1] = b[row][col + 1], b[row][col]
                case _:
                    return False
            return b  # if IndexError exception has not occurred, return copy of board with given shift
        except IndexError:
            return False
