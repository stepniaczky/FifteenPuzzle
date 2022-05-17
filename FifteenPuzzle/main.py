import sys
from check_args import check_args


def save(filename: str, _dict: dict):
    with open(filename, 'w') as file:
        for key in _dict.keys():
            file.write(f"{key}: {_dict[key]}\n")


def load(filename: str):
    with open(f"data/{filename}") as file:
        return file.readlines()


def main():
    args = sys.argv[1:]

    if len(args) != 5:
        exit("This script requires 5 positional arguments to start!")
    elif check_args(args) is False:
        exit()
    else:
        pass
        # board = Board(load(args[2]))
        # match args[0]:
        #     case 'dfs':
        #         strategy = DFS()
        #     case 'bfs':
        #         strategy = BFS()
        #     case 'astr':
        #         strategy = ASTR()
        # model = Strategy(board, args[0], args[1])
        # save(args[3], model.get_results)
        # save(args[4], model.get_info)


if __name__ == '__main__':
    main()
