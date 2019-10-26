import unittest
import sys
from objects import category
sys.path.append('..')


class CategoryListTests(unittest.TestCase):

    def get_api_categories(self):
        self.assertEqual(True, True)


class CategoryStorageTests(unittest.TestCase):

    def get_test_category(self):
        test_category = category(
            'TestCat',
            'TestCatParent',
            '',
            '',
            '10.33'
        )
        expected_category = 'TestCat'
        self.assertEqual(test_category.getName(), expected_category)


if __name__ == '__main__':
    unittest.main()
