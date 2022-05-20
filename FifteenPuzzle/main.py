import sys

from data.check_args import check_args
from data.file_manager import FileManager
from model.board import Board
from solvers.astr import ASTR
from solvers.bfs import BFS
from solvers.dfs import DFS


def strategy_choice(name: str, parameter: str):
    match name:
        case 'dfs':
            return DFS(parameter)
        case 'bfs':
            return BFS(parameter)
        case 'astr':
            return ASTR(parameter)
        case _:
            quit()


def main():
    args = sys.argv[1:]

    if len(args) != 5:
        quit("ArgumentError: This script requires 5 positional arguments to start!")
    elif check_args(args) is False:
        quit()
    else:
        fm = FileManager()
        board = Board(fm.load(args[2]))
        solver = strategy_choice(args[0], args[1])
        solver.solve(board)

        fm.save(args[3], solver.get_result())
        fm.save(args[4], solver.get_info())
        # fm.graph()
        # print(board)


if __name__ == '__main__':
    main()
