#b - генератор (итератор, который можно проходить)
b = (i for i in range(10))
print(b)
#Генератор можно пробежать в цикле  (но обойти можно лишь 1 раз)
for i in b:
    print(i, end=" ")
print("\n")


#Итератор можно получить из итерируемого объекта
c = iter([1, 2, 3])
#функция next переключает на следующий элемент итератора
for i in range(3):
    print(next(c), end=" ")
print("\n")


#yield - задает функцию генератор
# def f():
#     for i in [10, 20, 30]:
#         yield i
# for i in f():
#     print(i)


#функция factoriala - для функции генератора
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr *= i
        yield pr

s = fact(10)
# можно и так - for i in fact(10):
for i in s:
    print(i)
        