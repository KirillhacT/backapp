class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        #__class__ - имя класса
        return f"{self.__class__ }: {self.name}"

    def __str__(self):
        return f"{self.name}"


#__str__ - для отображения информации об объекте класса
#__repr__ - для отображения информации в режиме отладки
cat = Cat("Кошак")
print(cat)