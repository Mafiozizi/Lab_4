import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом."""
        self.rectangle = Rectangle(4.0, 3.0, "red")

    def test_area(self):
        """Проверка метода area() для установки правильной площади."""
        self.assertEqual(self.rectangle.area(), 12.0)

    def test_perimeter(self):
        """Проверка метода perimeter() для установки правильного периметра."""
        self.assertEqual(self.rectangle.perimeter(), 14.0)

    def test_set_size_length(self):
        """Проверка изменения длины прямоугольника."""
        self.rectangle.set_size(length=5.0)
        self.assertEqual(self.rectangle.length, 5.0)
        self.assertEqual(self.rectangle.width, 3.0)

    def test_set_size_width(self):
        """Проверка изменения ширины прямоугольника."""
        self.rectangle.set_size(width=2.0)
        self.assertEqual(self.rectangle.length, 4.0)
        self.assertEqual(self.rectangle.width, 2.0)

    def test_resize_scale(self):
        """Проверка изменения размеров с использованием масштаба."""
        self.rectangle.resize(scale=2.0)
        self.assertEqual(self.rectangle.length, 8.0)
        self.assertEqual(self.rectangle.width, 6.0)


if __name__ == "__main__":
    unittest.main()
