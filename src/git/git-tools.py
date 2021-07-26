import sys
from argparse import ArgumentParser
from errors.exceptions import InvalidArgumentException

REMOVE_BRANCH_COMMAND = "REMOVE_BRANCH"


def perform_command(args: list):
    command = args[1:2]
    args_parser = ArgumentParser()
    args_parser.add_argument("-c",
                             "--command",
                             required=True,
                             help="The command to execute. It can be one of: [remove-branches]")
    if command == REMOVE_BRANCH_COMMAND:
        perform_remove_branches(args[1:])
    else:
        raise InvalidArgumentException(f'Command: {command} is not a valid command')

    print(f'Subcommand: {command}')
    print(args)


def perform_remove_branches(args: list):
    print(args)


if __name__ == "__main__":
    perform_command(args=sys.argv)
