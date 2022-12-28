# class Weapon:
#     def __init__(self, name):
#         self.name = name
#
#     def take_damage(self):
#         print(f"Нанесен удар оружием {self.__class__}")
#
#     def show(self):
#         return f"name: {self.name}"
#
#     # def example(self):
#     #     abc = "Привет "
#     #     abc += self.name
#     #     print(abc)
#
# class Axe(Weapon):
#     def __init__(self, name, material):
#         super().__init__(name)
#         self.material = material
#
#     def show(self):
#         print(f"material axe is {self.material}")
#         return super().show()
#
#     # def example(self):
#     #     super().example()
#
# a = Axe("Топор", "Wood")
# # print(a.show())
# a.example()


class Geom:
    name = "Geom"
    def __init__(self, b):
        print(b)
        print("Инициализатор Geom")


class Line(Geom):
    def __init__(self, a, b):
        super().__init__(b)
        self.a = a

l = Line("a", 2)
print(l.a)
