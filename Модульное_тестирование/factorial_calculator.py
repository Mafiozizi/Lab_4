class FactorialCalculator:
    def __init__(self):
        """Инициализация класса. В данном случае не требуется дополнительных действий."""
        pass

    def factorial(self, n):
        """Вычисляет факториал числа n.

        Args:
            n (int): Целое неотрицательное число, для которого будет вычислен факториал.

        Returns:
            int: Факториал числа n.

        Raises:
            ValueError: Если n отрицательное.
        """
        if n < 0:
            # Если n отрицательное, выбрасываем исключение
            raise ValueError("Факториал не определён для отрицательных чисел.")
        elif n == 0 or n == 1:
            # Факториал 0 и 1 равен 1
            return 1
        else:
            result = 1
            # Вычисляем факториал, умножая значения от 2 до n
            for i in range(2, n + 1):
                result *= i
            return result

# Пример использования класса
if __name__ == "__main__":
    calculator = FactorialCalculator()

    try:
        # Запрашиваем ввод числа у пользователя
        num = int(input("Введите число для расчёта факториала: "))
        # Выводим результат
        print(f"Факториал {num} равен {calculator.factorial(num)}")
    except ValueError as e:
        # Обрабатываем исключение (неверный ввод или отрицательное число)
        print(e)
