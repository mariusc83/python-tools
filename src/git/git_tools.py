import git
import re
import sys

sys.path.insert(1, "/Users/marius.constantin/repos/python-scripts/src/git")
from argparse import ArgumentParser, Namespace
from errors.exceptions import InvalidArgumentException

REMOVE_BRANCH_COMMAND = "remove-branches"


def perform_command(args: list):
    command = args[1:2]
    args_parser = ArgumentParser()
    args_parser.add_argument("command",
                             help="The command to execute. It can be one of: [remove-branches]")
    parsed_args = args_parser.parse_args(command)
    if parsed_args.command == REMOVE_BRANCH_COMMAND:
        perform_remove_branches(args[2:])
    else:
        raise InvalidArgumentException(f'Command: {command} is not a valid command')


def perform_remove_branches(args: list):
    args_parser = ArgumentParser()
    args_parser.add_argument("-r",
                             "--regex",
                             help="The branch name regex on which to filter the branches to delete.")
    command_options = args_parser.parse_args(args)
    filter_branches_reg_ex = command_options.regex
    repository = git.Repo("./")
    branches_str = str(repository.git.branch())
    branches = map(lambda b: str(b).strip(), branches_str.split("\n"))
    to_remove_branches = filter_branches(branches, filter_branches_reg_ex)
    for branch in to_remove_branches:
        print(repository.git.branch("-D", branch))


def filter_branches(branches: list, filter_regex: str = None) -> list:
    if filter_regex:
        filter_in_reg_ex = re.compile(filter_regex)
        return list(filter(lambda branch: filter_in_reg_ex.match(branch), branches))
    return branches


if __name__ == "__main__":
    perform_command(args=sys.argv)
