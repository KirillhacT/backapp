#Замыкания (вложенная функция связана с переменной, объявленной не внутри нее)
def main_func(value):
    def inner_func():
        print(f"hello my friend, {value}")

    return inner_func

b = main_func("Egor")
b()

def upper(value):
    def middle(a):
        return value * a
    return middle

m = upper(10)
print(m(2))

#Замыкания 2
def average_numbers():
    numbers = []
    def inner(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)
    return inner

r1 = average_numbers()
print(r1(5))
print(r1(10))



def add(a, b, c):
    return a ** b + c
def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"функция {func.__name__  } вызывалась кол-во раз - {count}")
        return func(*args, **kwargs)
    return inner

a = counter(add)
print(a(5, 2, c=100))
print(a(10, 2, 1))
