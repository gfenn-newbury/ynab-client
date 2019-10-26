import unittest
import sys
import os
from api import auth
sys.path.append('..')


class AuthTest(unittest.TestCase):

    def test_auth_from_file(self):
        with open('./config/access.conf', 'w') as f:
            f.writeline('VGVzdAo=')
        auth()
        os.remove('./config/access.conf')
        self.assertEqual(auth.get_apikey(), 'Test')

    def test_auth_from_key(self):
        auth(key='Test')
        self.assertEqual(auth.get_apikey(), 'Test')


if __name__ == '__main__':
    unittest.main()
