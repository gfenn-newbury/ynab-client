import unittest
import json
import os
import sys
from ynab.lib import account_api


class ClientTests(unittest.TestCase):

    with open(
        os.path.join(
            sys.path[0],
            'tests',
            'data',
            "test_account_api.json"
        ),
        "r"
    ) as f:
        __test_data = json.load(f)

    def test_get_balance(self):
        account = account_api.Account(self.__test_data)
        self.assertEqual(
            account.get_balance()['Uncleared Balance'],
            self.__test_data['uncleared_balance']
            )
        self.assertEqual(
            account.get_balance()['Cleared Balance'],
            self.__test_data['cleared_balance']
        )

    def test_get_name(self):
        account = account_api.Account(self.__test_data)
        self.assertEqual(account.get_name(), self.__test_data['name'])

    def test_get_type(self):
        account = account_api.Account(self.__test_data)
        self.assertEqual(account.get_type(), self.__test_data['type'])

    def test_get_closed(self):
        account = account_api.Account(self.__test_data)
        self.assertEqual(account.get_closed(), self.__test_data['closed'])

    def test_get_account(self):
        account = account_api.Account(self.__test_data)
        expected = self.__test_data
        actual = account.get_account_json()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
