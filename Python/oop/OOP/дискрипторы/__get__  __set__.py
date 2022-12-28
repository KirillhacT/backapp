class Get_Set:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        return setattr(instance, self.name, value)

class Set:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    # def __set__(self, instance, value):
    #     return setattr(instance, self.name, value)


class Momo:
    x = Get_Set()
    y = Get_Set()
    z = Get_Set()
    S = Set()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.S = 1


a = Momo(66, 123)
print(a.__dict__)
print(a.x, a.y)
a.x, a.y = 1, 23
print(a.__dict__)
print(a.x, a.y)

# a.__dict__["S"] = 5
# print(a.__dict__)
# print(a.S)


