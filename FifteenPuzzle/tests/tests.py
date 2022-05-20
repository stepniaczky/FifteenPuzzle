from os import remove
import unittest
from model.board import Board
from data.check_args import check_args


class CheckArgsCase(unittest.TestCase):
    proper_args = ['bfs', 'DLRU', 'test_board.txt', 'results.txt', 'info.txt']

    def test_proper_strategy(self):
        open(f'data/files/{self.proper_args[2]}', 'a').close()
        self.assertIsNone(check_args(self.proper_args))
        remove(f'data/files/{self.proper_args[2]}')

    def test_wrong_strategy(self):
        args = self.proper_args.copy()
        args[0] = 'bffs'
        with self.assertRaises(SystemExit) as e:
            check_args(args)
        self.assertEqual(e.exception.__str__(),
                         "ArgumentError: First argument must equals one of: 'dfs', 'bfs' or 'astr'!")

    def test_proper_parameters(self):
        args = self.proper_args.copy()
        open(f'data/files/{args[2]}', 'a').close()
        self.assertIsNone(check_args(args))

        args[0] = 'dfs'
        self.assertIsNone(check_args(args))

        args[0] = 'astr'
        args[1] = 'hamm'
        self.assertIsNone(check_args(args))
        args[1] = 'manh'
        self.assertIsNone(check_args(args))
        remove(f'data/files/{args[2]}')

    def check_wrong_parameters(self, args):
        with self.assertRaises(SystemExit) as e:
            check_args(args)
        self.assertEqual(e.exception.__str__(),
                         f"ArgumentError: Strategy: '{args[0]}' cannot be used with parameter: '{args[1]}'!")

    def test_wrong_parameters(self):
        args = self.proper_args.copy()
        open(f'data/files/{args[2]}', 'a').close()
        args[1] = 'manh'
        self.check_wrong_parameters(args)

        args[1] = 'hamm'
        self.check_wrong_parameters(args)

        args[0] = 'dfs'
        self.check_wrong_parameters(args)

        args[1] = 'bfs'
        self.check_wrong_parameters(args)

        args[0] = 'astr'
        args[1] = 'LRDU'
        self.check_wrong_parameters(args)
        remove(f'data/files/{args[2]}')

    def test_files_extension(self):
        args = self.proper_args.copy()
        args[2] = 'test_board.ttx'
        with self.assertRaises(SystemExit) as e:
            check_args(args)
        self.assertEqual(e.exception.__str__(), f"ArgumentError: File name: '{args[2]}' must ends with '.txt'!")

    def test_file_existence(self):
        with self.assertRaises(SystemExit) as e:
            check_args(self.proper_args)
        self.assertEqual(e.exception.__str__(),
                         f"ArgumentError: File: '{self.proper_args[2]}' with initial board "
                         f"does not exist in '/data/files' directory!")


class BoardTestCase(unittest.TestCase):
    initial_board = ['4 4', '0 1 2 3', '4 5 6 7', '8 9 10 11', '12 13 14 15']
    diff_dimension_board = ['3 3', '1 2 0', '4 5 3', '7 8 6']
    solved_board = ['4 4', '1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 0']

    def test_init_good(self):
        self.assertTrue(Board(self.initial_board))

    def test_init_diff_dimensions(self):
        self.assertTrue(Board(self.diff_dimension_board))

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
        board = Board(self.solved_board)
        self.assertTrue(board.is_solved())

    def test_solved_incorrectly(self):
        board = Board(self.initial_board)
        self.assertFalse(board.is_solved())

    def test_get_empty_cell(self):
        board = Board(self.initial_board)
        self.assertEqual(board.get_xy(0), (0, 0))

    # tests moves that should return proper board copy
    def test_move_good(self):
        b = Board(self.initial_board)  # empty cell is in top left corner
        row, col = b.get_xy(0)

        b = b.move('D')
        self.assertEqual(b.get_xy(0), (row + 1, col))

        b = b.move('R')
        self.assertEqual(b.get_xy(0), (row + 1, col + 1))

        b = b.move('U')
        self.assertEqual(b.get_xy(0), (row, col + 1))

        b = b.move('L')
        self.assertEqual(b.get_xy(0), (row, col))

    # tests moves that should return False
    def test_move_bad(self):
        b1 = Board(self.initial_board)  # top left corner ['4 4', '0 1 2 3', '4 5 6 7', '8 9 10 11', '12 13 14 15']
        self.assertFalse(b1.move('U'))
        self.assertFalse(b1.move('L'))

        b2 = Board(self.solved_board)
        self.assertFalse(b2.move('D'))
        self.assertFalse(b2.move('R'))

    def test_diff_dimension_solved(self):
        b = Board(self.diff_dimension_board)
        b = b.move('D')
        b = b.move('D')
        self.assertTrue(b.is_solved())

    def test_hamm_dist(self):
        b = Board(self.initial_board)
        self.assertEqual(b.get_dist('hamm'), 16)

        b = Board(self.solved_board)
        self.assertEqual(b.get_dist('hamm'), 0)

    def test_manh_dist(self):
        b = Board(self.initial_board)
        self.assertEqual(b.get_dist('manh'), 24)

        b = Board(self.solved_board)
        self.assertEqual(b.get_dist('manh'), 0)

    def test_correct_board_getter(self):
        b = Board(self.initial_board)
        self.assertFalse(b.is_solved())

        b = b.get_correct_board()
        self.assertTrue(b.is_solved())

        b = Board(self.diff_dimension_board)
        b = b.get_correct_board()
        self.assertTrue(b.is_solved())


if __name__ == '__main__':
    unittest.main()
