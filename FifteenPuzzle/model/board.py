import copy


class Board:

    def __init__(self, initial: list):
        self.initial_list = initial
        try:
            self.r, self.c = list(map(int, initial[0].split()))  # number of rows and columns
            self.SIZE = self.r * self.c  # number of elements in board
            self.board = [list(map(int, row.split())) for row in initial[1:]]  # board list with integer values
        except ValueError:
            quit("BoardError: File with initial board contains letters!")
        except IndexError:
            quit("BoardError: File with initial board is empty!")
        self.check_dimensions()
        self.check_elements()
        self.parent = None  # board state before last movement
        self.movement = ''  # the direction to move parent board to current state
        self.steps = 0

    # prints board
    def __str__(self):
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

    # returns deep copy of board object
    def __copy__(self):
        b = eval(self.__repr__())
        b.board = copy.deepcopy(self.board)
        b.parent = self.parent
        b.movement = self.movement
        return b

    # returns hash value of actual state of board
    def __hash__(self):
        return hash(str(self.board))

    # required by Priority Queue in ASTR strategy for comparing elements in queue
    def __lt__(self, other):
        return True

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

    # returns row and column of given element in board
    def get_xy(self, element: int) -> tuple:
        for i, row in enumerate(self.board):
            if element in row:
                return i, row.index(element)

    # returns correctly solved board with the same dimensions
    def get_correct_board(self):
        b = self.__copy__()
        b.board = [[col for col in range(1 + (row * self.c), 1 + self.c + (row * self.c))] for row in range(self.r)]
        b.board[self.r - 1][self.c - 1] = 0
        return b

    # checks if board is solved correctly, which means that board elements
    # starts with 1 then iterates one by one to self.SIZE - 1 and the last element of board equals 0
    # returns True if board is solved, else False
    def is_solved(self) -> bool:
        return self.board == self.get_correct_board().board

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

    # returns distance in the given metric
    def get_dist(self, metric_name: str) -> int:
        if metric_name == 'hamm':
            return self.__hamm_dist()
        else:
            return self.__manh_dist()

    # returns hamming distance between board cells and their correctly indexes
    def __hamm_dist(self) -> int:
        dist = 0

        for i, row in enumerate(self.board, start=1):
            for j, col in enumerate(row, start=1):

                if i * j == self.SIZE:
                    return dist if col == 0 else dist + 1

                elif col != (i - 1) * self.c + j:
                    dist += 1

    # returns manhattan distance between board cells and their correctly indexes (skipping zero element)
    def __manh_dist(self) -> int:
        dist = 0
        for row in range(self.r):
            for col in range(self.c):

                if (value := self.board[row][col]) != 0:
                    value -= 1
                    x = value % self.c
                    y = value // self.r
                    dist += abs(x - col) + abs(y - row)

        return dist
