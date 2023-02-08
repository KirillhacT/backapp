import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        #!r для получения стандартного представления отображаемых атрибутов
        return f"Vector ({self.x!r}, {self.y!r})"

    def __abs__(self):
        # Абсолютная величина
        return math.hypot(self.x, self.y)

    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        #Сложение векторов
        x = self.x + other.x
        y = self.y + other.y
        return self.__class__(x, y)
    def __mul__(self, scalar):
        # Умножение на скаляр
        return self.__class__(self.x * scalar, self.y * scalar)

v1 = Vector(2, 3)
v2 = Vector(1, 5)
# print(v3 := v1 + v2)
# print(v3 * 3)

