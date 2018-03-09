import unittest
from test_class import YourDict

class Unittests(unittest.TestCase):
'''Unittesting to ensure that instance.a == instance['a'] and vice versa'''

    def test_assert_equal(self):
        '''Test Case 1: dict[test] == dict.test'''
        test_dict = YourDict()
        test_dict['equal'] = 3
        self.assertEqual(test_dict.equal, test_dict['equal'])

    def test_equal_assert(self):
        '''Test Case 2: dict.test == dict[test]'''
        test_dict = YourDict()
        test_dict.equal = 3
        self.assertEqual(test_dict.equal, test_dict['equal'])


if __name__ == '__main__':
    unittest.main()





