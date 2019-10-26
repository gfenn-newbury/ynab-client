import unittest
import api


class AuthTest(unittest.TestCase):

    def test_auth_from_file(self):
        with open('./config/access.conf', 'w') as f:
            f.writeline('VGVzdAo=')
        api.auth()
        self.assertEqual(api.auth.get_apikey(), 'Test')

    def test_auth_from_key(self):
        api.auth(key='Test')
        self.assertEqual(api.auth.get_apikey(), 'Test')


if __name__ == '__main__':
    unittest.main()
