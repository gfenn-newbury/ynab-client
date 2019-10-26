import unittest
import os
from ... import ynab


class AuthTest(unittest.TestCase):

    def test_auth_from_file(self):
        with open('./config/access.conf', 'w') as f:
            f.writeline('VGVzdAo=')
        ynab.auth()
        os.remove('./config/access.conf')
        self.assertEqual(ynab.auth.get_apikey(), 'Test')

    def test_auth_from_key(self):
        ynab.auth(key='Test')
        self.assertEqual(ynab.auth.get_apikey(), 'Test')


if __name__ == '__main__':
    unittest.main()
