import unittest
import json
import os
import sys
from ynab import core


class ClientTests(unittest.TestCase):

    with open(
        os.path.join(
            sys.path[0],
            'tests',
            'data',
            "test_core.json"
        ),
        "r"
    ) as f:
        __test_data = json.load(f)

    def test_get_accounts(self):
        client = core.Api(budgets=self.__test_data)
        accounts = client.get_accounts(
            budget_id=self.__test_data[0]['budget']['id']
        )
        self.assertEqual(
            accounts,
            self.__test_data[0]['budget']['accounts']
        )

    def test_get_categories(self):
        test_data = self.__test_data
        budget_id = test_data[0]['budget']['id']
        client = core.Api(budgets=test_data)
        actual = client.get_categories(budget_id=budget_id)
        expected = test_data[0]['budget']['categories']
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
