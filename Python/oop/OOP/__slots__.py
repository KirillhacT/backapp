class Point:
    #В slots указываются локальные свойства, которые могут существовать в экземплярах
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y
pt = Point(10, 20)
# print(pt.__dict__) #Возвращает поля объекта
print(pt.x, pt.y)