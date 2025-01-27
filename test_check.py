import unittest
from CW_check import check


# Чтобы проверять работу функции, нужно прописать, что будет делать эта функция.
# Нам нужно проверить, что четные числа будут возвращать значение True.
# Поэтому прописываем assertTrue и в скобках указываем название функции check с указанием в скобках какого-либо числа
class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(not check(255))
        self.assertTrue(check(6))
        self.assertTrue(check(222))
        self.assertTrue(not check(3))
        self.assertFalse(check(55))


if __name__ == '__main__':
    unittest.main()
