#Магические методы для сравнения
# __eq__(self, other) => self == other
# __ne__(self, other) => self != other
# __lt__(self, other) => self < other
# __gt__(self, other) => self > other
# __le__(self, other) => self <= other
# __ge__(self, other) => self >= other

# Магические методы для вычислений
# __add__(self, other) => self + other
# __sub__(self, other) => self — other
# __mul__(self, other) => self * other
# __floordiv__(self, other) => self // other
# __truediv__(self, other) => self / other
# __mod__(self, other) => self % other
# __pow__(self, other) => self ** other

class TextClass:
    def __init__(self, text):
        self.text = text

    def __eq__(self, other): #Метод сравнения на равенство ==
        return self.text.lower() == other.text.lower()

    def __lt__(self, other): #Метод на сравнения больше меньше <>
        return len(self.text) < len(other.text)
first = TextClass("Na")
second = TextClass("Nda")
print(first == second)
print(first < second)
print("\n")

class Integer:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __lt__(self, other):
        return self.x < other.x

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __floordiv__(self, other):
        return self.x // other.x

    def __truediv__(self, other):
        return self.x / other.x

    def __mod__(self, other):
        return self.x % other.x

    def __pow__(self, other):
        return self.x ** other.x

    def __str__(self):
        return f"This number is {self.x}"
one = Integer(10)
two = Integer(3)
print(one + two)
print(one - two)
print(one * two)
print(one // two)
print(one / two)
print(one % two)
print(one ** two)

print(one != two)
print(one > two)

# class TwoIntegers(Integer):
#     def __init__(self, x):
#         super().__init__(x)
#
# num1 = TwoIntegers(123)
# num2 = TwoIntegers(3)
# print(num1 > num2)




