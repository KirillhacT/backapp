import math
import traceback

class Circle:
    """Класс, который описывает поведение окружности"""

    def __init__(self, radius: float) -> None:
        """Инициализация параметров окружности, radius - радиус окружности"""
        self.radius = radius

    def get_area(self) -> float:
        """Вычисляет площадь круга"""
        return math.pi * self.radius ** 2

    def get_lenght(self) -> float:
        """Вычисляет длину окружности"""
        return 2 * math.pi * self.radius

    def get_diametr(self) -> float:
        """Вычисляет диаметр окружности"""
        return 2 * self.radius

first_circle = Circle(radius=10)
second_circle = Circle(radius=15)

# print(round(first_circle.get_area(), 5))
# print(round(second_circle.get_diametr()))
# print(__name__)

#try / except

def divide_two_numbers(first_number: float, second_number: float) -> float:
    assert second_number != 0  #Проверка на истинность, если не прошел ошибка
    if second_number == 13:
        raise ValueError("Плохое число, выберите другое")
    try:
        result = first_number / second_number
        return result
    except Exception as ex:
        print(f'Ошибка - {ex}')
        exit()
#Мы можем возбудить исключение и сразу же обработать его
try:
    print(divide_two_numbers(1, 13))
except ValueError as valueError:
    print(f"Ошибка - {valueError}")
    print("Мы поняли, больше не будем)")
    msg = traceback.format_exc() #Информация об ошибках
    # print(msg)
#Основные типы ошибок
# KeyError - ошибка ключа
# TypeError - ошибка типа
# IndexError - ошибка индекса
# ValueError - ошибка значения