class Vector:
    MAX_COORD = 100
    MIN_COORD = 0

    # метод класса работает с атрибутами класса (к локальным экземплярам не может)
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        # if Vector.validate(x) and Vector.validate(y):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v1 = Vector(413, 14)
print(v1.get_coord())
# Либо через класс - тоже самое
# res = Vector.get_coord(v1)
# print(res)

# Для классного метода не нужна ссылка на экземпляр
print(Vector.validate(10))

# staticmethod - не нужна ссылка на экземпляр класса
a = Vector.norm2(10, 2)
print(a)
