import unittest
from mymodule import add_intergers
from mymodule import assert_int

class TestMyModule(unittest.TestCase):

    def test_add_intergers_with_intergers(self):
        self.assertEqual(add_intergers(1, 2), 3)

    def test_add_intergers_negative(self):
        n1 = -2
        n2 = 0
        expected_value = n1 + n2
        self.assertEqual(
            add_intergers(n1, n2),
            expected_value
        )

    def test_add_intergers_error_if_not_int(self):
        self.assertRaises(TypeError, add_intergers, 13.3, 3.5)

    def test_assert_int_int_raises_no_error(self):
        for n in range(-100, 101):
            self.assertTrue(assert_int(n))

    def test_assert_int_non_int_raises_typeerror(self):
        self.assertRaises(TypeError, assert_int, 1, 1.3)

if __name__ == '__main__':
    unittest.main()

