import unittest
from git_tools import perform_command
from git_tools import filter_branches
from errors.exceptions import InvalidArgumentException


class GitToolsTest(unittest.TestCase):
    def test_perform_command_invalid_command(self):
        with self.assertRaises(InvalidArgumentException):
            perform_command(["command", "invalid_command"])

    def test_filter_branches_no_reg_ex(self):
        branches_list = ["main", "mconstantin/summ-1000", "mconstantin/summ-1001"]
        processed_branches_list = filter_branches(branches_list)
        self.assertListEqual(branches_list, processed_branches_list)

    def test_filter_branches_with_reg_ex_format1(self):
        branches_list = ["main", "mconstantin/summ-1000", "mconstantin/summ-1001"]
        processed_branches_list = filter_branches(branches_list, "(.*)\\/summ-10(.*)")
        expected_branches = ["mconstantin/summ-1000", "mconstantin/summ-1001"]
        self.assertListEqual(expected_branches, processed_branches_list)

    def test_filter_branches_with_reg_ex_format2(self):
        branches_list = ["main", "mconstantin/summ-1000", "mconstantin/summ-1001"]
        processed_branches_list = filter_branches(branches_list, "(.*)")
        expected_branches = ["main", "mconstantin/summ-1000", "mconstantin/summ-1001"]
        self.assertListEqual(expected_branches, processed_branches_list)

    def test_filter_branches_with_reg_ex_format3(self):
        branches_list = ["mconstantin/summ-10/test",
                         "mconstantin/summ-23/test/test",
                         "mconstantin/summ-1000/wrerwef",
                         "mconstantin/summ-1001/dsad"]
        processed_branches_list = filter_branches(branches_list, "(.*)\\/summ-(\\d){2}\\/(.*)")
        expected_branches = ["mconstantin/summ-10/test", "mconstantin/summ-23/test/test"]
        self.assertListEqual(expected_branches, processed_branches_list)

    def test_filter_branches_with_reg_ex_format3(self):
        branches_list = ["mconstantin/summ-10/test",
                         "mconstantin/summ-23/test/test",
                         "mconstantin/summ-1000/wrerwef",
                         "mconstantin/summ-1001/dsad"]
        processed_branches_list = filter_branches(branches_list, "^mconstantin(.*)")
        expected_branches = ["mconstantin/summ-10/test",
                             "mconstantin/summ-23/test/test",
                             "mconstantin/summ-1000/wrerwef",
                             "mconstantin/summ-1001/dsad"]
        self.assertListEqual(expected_branches, processed_branches_list)


if __name__ == '__main__':
    unittest.main()
