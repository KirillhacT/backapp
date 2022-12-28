import math


class Counter:
    def __init__(self):
        self.__value = 0
        self.__count = 0

    def __call__(self, value, *args, **kwargs):
        self.__value += value
        self.__count += 1
        return (self.__value, self.__count)


#Классы с методом __call__ - функторы
#Когда мы прописываем круглые скобки, то вызывается метод __call__
c = Counter()
print(c(0))
print(c(23))
print(c(100))

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         #isinstance - провереяет, может ли существовать аргумент передаваемого типа данных
#         if not isinstance(args[0], str):
#             raise TypeError("Аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
#
# s1 = StripChars("!:.,;&? ")
# result = s1(" Hello world! ")
# new_res = f"({result})"
# print(new_res)

class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

@Derivate
def df_sin(x):
    return math.sin(x)

# df_sin2 = Derivate(df_sin)
# print(df_sin2(math.pi/3))
print(df_sin(math.pi/6))


