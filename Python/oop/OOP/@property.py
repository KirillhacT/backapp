class Person:
    def __init__(self, name, old) -> None:
        self.__name = name
        self.__old = old
    @property
    def old(self):
        return self.__old

    # def get_old(self):
    #     return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter #Вызывается, когда удаляется свойство
    def old(self):
        del self.__old

    # def get_old(self, old):
    #     self.__old = old

    # old = property(get_old, set_old)

me = Person("Egor", 24)
# me.set_old(10)
# print(me.get_old())
#Через геттеры и сеттеры делать неудобно, так как для каждого атрибута нужны свои функции
# print(me.old)
# me.old = 123
# print(me.old, me.__dict__)
print(me.old)
me.old = 232
print(me.old)
del me.old
me.old = 1
print(me.__dict__)





