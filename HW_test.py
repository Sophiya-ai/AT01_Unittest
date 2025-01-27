import unittest
from HW import rest_of_division


class TestClass(unittest.TestCase):
    def test_rest_of_division(self):
        self.assertEqual(rest_of_division(10, 5), 0)
        self.assertNotEqual(rest_of_division(20, 3), 3)
        self.assertEqual(rest_of_division(33, 5), 3)

    def test_raise(self):
        self.assertRaises(ValueError, rest_of_division, 33, 0)


if __name__ == '__main__':
    unittest.main()
