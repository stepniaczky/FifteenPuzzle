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
    def is_solved(self) -> bool:
        try:
            for i, element in enumerate(self.board, start=1):
                if i == self.SIZE - 1:
                    assert element == 0
                assert element == 1
            return True
        except AssertionError:
            return False

