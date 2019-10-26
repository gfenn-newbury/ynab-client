import unittest
from ynab.objects import category


class TestYnabObjects(unittest.TestCase):

    def test_category_name(self):
        test_category = category('TestCat', 'TestCatParent', '', '', '10.33')
        expected_category = 'TestCat'
        self.assertEqual(test_category.getName(), expected_category)


if __name__ == '__main__':
    unittest.main()
