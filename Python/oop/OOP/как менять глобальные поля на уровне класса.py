class Point:
    MAX_VALUE = 999
    MIN_VALUE = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def set_attribute(self, number):
    #     self.MIN_VALUE = number
    # Значение MIN_VALUE в данном случае устанавливается локально для данного экземпляра
    # глобальное значение его останется тем же

    @classmethod
    def set_attribute(cls, number) -> None:
        cls.MIN_VALUE = number


poin = Point(1, 2)
# print(poin.MIN_VALUE)
poin.set_attribute(78)
print(poin.__dict__)
print(Point.__dict__)











