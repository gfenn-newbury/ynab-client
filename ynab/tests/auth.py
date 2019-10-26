import unittest
import os


class AuthTest(unittest.TestCase):

    from ..api import auth

    def test_auth_from_file(self):
        with open('./config/access.conf', 'w') as f:
            f.writeline('VGVzdAo=')
        self.auth()
        os.remove('./config/access.conf')
        self.assertEqual(self.auth.get_apikey(), 'Test')

    def test_auth_from_key(self):
        self.auth(key='Test')
        self.assertEqual(self.auth.get_apikey(), 'Test')


if __name__ == '__main__':
    unittest.main()
