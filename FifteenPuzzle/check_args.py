from os.path import exists

"""
Checks every argument that is passed to the script
1 argument: Strategy that equals one of ['dfs', 'bfs', 'astr']
2 argument: Parameter that equals 'hamm', 'manh' or 4 length combination of letters: ['D', 'L', 'R', 'U'], 
    eg. 'LUDR', 'RDUL' (every letter can appear only once!)
3 argument: Name of the file with initial board that exists in '/data/' directory
4 argument: Name of the file to which results will be saved (in '/data/' dir)
5 argument: Name of the file to which additional information will be saved  (in '/data/' dir)
"""


def check_args(args):
    try:
        # checks strategy value
        strategy: str = args[0]
        assert strategy in ['dfs', 'bfs', 'astr'], \
            "ArgumentError: First argument must equals one of: 'dfs', 'bfs' or 'astr'!"

        # checks parameter value
        parameter: str = args[1]
        if strategy in ['dfs', 'bfs']:
            assert sorted(parameter) == ['D', 'L', 'R', 'U'], \
                f"ArgumentError: Strategy: '{strategy}' cannot be used with parameter: '{parameter}'!"
        else:
            assert parameter in ['hamm', 'manh'], \
                f"ArgumentError: Strategy: '{strategy}' cannot be used with parameter: '{parameter}'!"

        # checks files extension
        for i in range(2, 4):
            assert args[i].endswith('.txt'), \
                f"ArgumentError: File name: '{args[i]}' must ends with '.txt'!"

        # checks if initial board file exists in /data/ directory
        assert exists(f'data/{args[2]}'), \
            f"File: '{args[2]}' with initial board does not exist in '/data/' directory!"

    # if anything went wrong, quits program with the appropriate message
    except AssertionError as msg:
        exit(msg)
