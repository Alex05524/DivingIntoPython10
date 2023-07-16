# Класс исключения для обработки ошибок в генераторе чисел Фибоначчи
class FibonacciError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Функция-генератор чисел Фибоначчи
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования
try:
    # Создание генератора чисел Фибоначчи
    fibonacci = fibonacci_generator()
    
    # Генерация первых 10 чисел Фибоначчи
    for _ in range(10):
        print(next(fibonacci))
except FibonacciError as e:
    print("Ошибка в генераторе чисел Фибоначчи:", e.message)