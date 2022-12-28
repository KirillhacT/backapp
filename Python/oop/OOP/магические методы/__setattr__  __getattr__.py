class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value): #key - аргумент, которому присваивают, value - его значение
        print("__setattr__")
        if key == "y":
            value = 10
            self.__dict__[key] = value
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        # print("__getattr__ " + item)
        return False

    def __delattr__(self, item):
        print("__delattr__ " + item)
        object.__delattr__(self, item)

#__setattr__ - если идет присваивание какому-либо аргументу в классе
#__getattr__ - вызывается, если идет обращение к несуществующему атрибуту
#__delattr__ - вызывается, когда удаляется какой-либо атрибут класса

poin = Point(20, 1) #В данном случае у нас присваивание x и y
print(poin.y)
print(poin.yy)
del poin.x