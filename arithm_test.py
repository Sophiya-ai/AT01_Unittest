import unittest
from CW_arithm_ab import add, subtract, multiply, divide


# Прописываем класс с указанием в скобках родительского класса.
# Существует несколько базовых классов (компонентов), с которыми мы можем работать. Это TestCase, TestSuite и TestRunner.
# TestSuite — это группа тестов, объединенных для совместного выполнения.
# TestRunner — это компонент, запускающий тесты и выводит те или иные результаты.
# TestCase — это класс, содержащий различные методы. Например, assertEqual.#
# Функция assertEqual — это функция, проверяющая равенства. Этот метод проверяет, равны ли два значения.
# Обычно он используется в тестах для автоматической проверки того, что результат выполнения кода соответствует
# ожидаемому значению. Мы указываем использование функции с определенными значениями и указываем,
# какой должен быть результат; если результат не соответствует, тест не будет пройден.

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertEqual(multiply(3, 6), 18)
        self.assertNotEqual(multiply(2, 5), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertNotEqual(divide(20, 10), 3)

    # вызовем функцию assertRaises, которая будет проверять, что функция,
    # которая будет здесь указана, будет вызывать именно исключения.
    # В круглых скобках мы указали, какую ошибку нужно проверять (ValueError),
    # функцию divide и через запятую значения для переменных
    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)


if __name__ == '__main__':
    unittest.main()
