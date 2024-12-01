import unittest
from factorial_calculator import FactorialCalculator

class TestFactorialCalculator(unittest.TestCase):

    def setUp(self):
        """Настройка, выполняемая перед каждым тестом."""
        self.calculator = FactorialCalculator()

    def test_factorial_zero(self):
        """Проверка факториала 0."""
        self.assertEqual(self.calculator.factorial(0), 1)

    def test_factorial_one(self):
        """Проверка факториала 1."""
        self.assertEqual(self.calculator.factorial(1), 1)

    def test_factorial_two(self):
        """Проверка факториала 2."""
        self.assertEqual(self.calculator.factorial(2), 2)

    def test_factorial_three(self):
        """Проверка факториала 3."""
        self.assertEqual(self.calculator.factorial(3), 6)

    def test_factorial_four(self):
        """Проверка факториала 4."""
        self.assertEqual(self.calculator.factorial(4), 24)

    def test_factorial_five(self):
        """Проверка факториала 5."""
        self.assertEqual(self.calculator.factorial(5), 120)

    def test_factorial_negative(self):
        """Проверка, что выбрасывается исключение при вводе отрицательного числа."""
        with self.assertRaises(ValueError):
            self.calculator.factorial(-1)

    def test_factorial_large(self):
        """Проверка факториала для более крупных чисел."""
        self.assertEqual(self.calculator.factorial(10), 3628800)


if __name__ == "__main__":
    unittest.main()
