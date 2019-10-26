import unittest
import os
import api


class AuthTest(unittest.TestCase):

    def test_auth_from_file(self):
        with open('./config/access.conf', 'w') as f:
            f.writeline('VGVzdAo=')
        api.auth()
        os.remove('./config/access.conf')
        self.assertEqual(api.auth.get_apikey(), 'Test')

    def test_auth_from_key(self):
        api.auth(key='Test')
        self.assertEqual(api.auth.get_apikey(), 'Test')


if __name__ == '__main__':
    unittest.main()
