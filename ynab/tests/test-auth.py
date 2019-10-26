import unittest
import os
from ynab import api


class AuthTest(unittest.TestCase):

    def test_auth_from_file(self):
        os.mkdir('./config')
        with open('./config/access.conf', 'w') as f:
            f.write('VGVzdAo=')
        ynab = api.auth()
        self.assertEqual(ynab.get_apikey().rstrip(), b'Test')

    def test_auth_from_key(self):
        ynab = api.auth(key='Test')
        self.assertEqual(ynab.get_apikey(), 'Test')


if __name__ == '__main__':
    unittest.main()
