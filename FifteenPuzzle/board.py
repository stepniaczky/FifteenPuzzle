class Board:

    def __init__(self, initial: list):
        self.r, self.c = initial[0].split()
        self.board = [list(row.split()) for row in initial[1:]]
        self.check_size()

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
