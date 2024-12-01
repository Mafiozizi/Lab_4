class Rectangle:
    def __init__(self, length: float, width: float, color: str):
        """Инициализация прямоугольника с длиной, шириной и цветом."""
        self.length = length
        self.width = width
        self.color = color

    def area(self) -> float:
        """Возвращает площадь прямоугольника."""
        return self.length * self.width

    def perimeter(self) -> float:
        """Возвращает периметр прямоугольника."""
        return 2 * (self.length + self.width)

    def set_size(self, length: float = None, width: float = None) -> None:
        """Изменяет длину и/или ширину прямоугольника."""
        if length is not None:
            self.length = length
        if width is not None:
            self.width = width

    def resize(self, scale: float) -> None:
        """Изменяет размеры прямоугольника на данный коэффициент масштаба."""
        self.length *= scale
        self.width *= scale

