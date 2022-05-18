import unittest
from board import Board


class BoardTestCase(unittest.TestCase):
    initial_board = ['4 4', '0 1 2 3', '4 5 6 7', '8 9 10 11', '12 13 14 15']

    def test_init_good(self):
        self.assertTrue(Board(self.initial_board))

    def test_init_incorrect_dimensions(self):
        b = self.initial_board.copy()
        b[0] = '3 4'  # incorrect board dimensions
        with self.assertRaises(SystemExit) as e:
            Board(b)  # should raise SystemExit
        self.assertEqual(e.exception.__str__(), 'BoardError: Given number of board rows is incorrect!')
        b[0] = '4 3'
        with self.assertRaises(SystemExit) as e:
            Board(b)  # should raise SystemExit
        self.assertEqual(e.exception.__str__(), 'BoardError: Given number of board columns is incorrect!')

    def test_init_element_out_of_range(self):
        b = self.initial_board.copy()
        b[1] = '0 1 2 16'  # 16 is out of range [0, 15]
        with self.assertRaises(SystemExit) as e:
            Board(b)  # should raise SystemExit
        self.assertEqual(e.exception.__str__(), 'BoardError: Value of the board element is out of range [0, 15]!')

    def test_init_duplicate_elements(self):
        b = self.initial_board.copy()
        b[1] = '0 0 2 3'  # 0 shouldn't appears twice
        with self.assertRaises(SystemExit) as e:
            Board(b)  # should raise SystemExit
        self.assertEqual(e.exception.__str__(), 'BoardError: Board has duplicate element values!')

    def test_solved_correctly(self):
        b = ['4 4', '1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 0']
        board = Board(b)
        self.assertTrue(board.is_solved())

    def test_solved_incorrectly(self):
        board = Board(self.initial_board)
        self.assertFalse(board.is_solved())

    def test_get_empty_cell(self):
        board = Board(self.initial_board)
        self.assertEqual(board.get_empty_cell(), (0, 0))

    # tests moves that should return proper board copy
    def test_move_good(self):
        b = Board(self.initial_board)
        row, col = b.get_empty_cell()

        b.board = b.move('U')
        self.assertEqual(b.get_empty_cell(), (row + 1, col))

        b.board = b.move('L')
        self.assertEqual(b.get_empty_cell(), (row + 1, col + 1))

        b.board = b.move('D')
        self.assertEqual(b.get_empty_cell(), (row, col + 1))

        b.board = b.move('R')
        self.assertEqual(b.get_empty_cell(), (row, col))

    # tests moves that should return False
    def test_move_bad(self):
        b1 = Board(self.initial_board)  # top left corner ['4 4', '0 1 2 3', '4 5 6 7', '8 9 10 11', '12 13 14 15']
        self.assertFalse(b1.move('D'))
        self.assertFalse(b1.move('R'))

        bottom_right_corner = ['4 4', '1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 0']
        b2 = Board(bottom_right_corner)
        self.assertFalse(b2.move('U'))
        self.assertFalse(b2.move('L'))


if __name__ == '__main__':
    unittest.main()
