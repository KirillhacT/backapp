class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self.__y = y

        self.__a = self.__b = 0
    def set_coord(self, x, y) -> None: #сеттер
        if self.__check_value(x) and self.__check_value(y):
            self.__a = x
            self.__b = y
        else:
            raise ValueError("Значения указаны некорректно")

    @classmethod
    def __check_value(cls, x) -> bool:
        return type(x) in (int, float)

    def get_coord(self) -> tuple: #геттер
        return self.__a, self.__b

#set_coord - сеттер
#get_coord - геттер
pt = Point(1, 2)
print(pt._x)
# pt.__y = "hacked"
# print(pt._x, pt.__y)

pt.set_coord(12, 13)
print(pt.get_coord())

print(pt._Point__a) #из приватного поля можно вытащить значение, но это крайне не рекомендуется

#переменная - public -> доступен везде

#_переменная - protected -> доступен внутри класса и во всех дочерних классах
#не защищает от обращения, но предостерегает программиста

#__переменная - private -> доступен только внутри класса
#нельзя обращаться вне класса
















