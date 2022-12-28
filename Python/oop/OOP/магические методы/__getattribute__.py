class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item): #item принимает в себя атрибут, к которому обращаются
        print("__getattribute__")
        if item == "x":
            raise ValueError("Обращение к атрибуту x запрещен")
        return object.__getattribute__(self, item)


#__getattribute__ - срабатывает, когда идет обращение к какому либо атрибуту через экземпляр класса

poin = Point(20, 1)
# a = poin.x # в данном случае выскочит ошибка, так как обращение к атрибуту x запрещено
b = poin.y #Есть обращение к атрибуту, следовательно сработает метод
print(b)