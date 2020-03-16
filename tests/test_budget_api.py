import unittest
import json
import os
import sys
from ynab.lib import account_api


class ClientTests(unittest.TestCase):

    with open(os.path.join(sys.path[0],'tests','data',"test_budget_api.json"),"r") as f:
        __test_data = json.load(f)

    def test_get_budget_id(self):
        raise NotImplementedError

    def test_get_budget_json(self):
        raise NotImplementedError

    def test_get_category_json_list(self):
        raise NotImplementedError

    def test_get_category_object_list(self):
        raise NotImplementedError

    def test_get_account_json_list(self):
        raise NotImplementedError

    def test_get_acount_object_list (self):
        raise NotImplementedError


if __name__ == '__main__':
    unittest.main()
