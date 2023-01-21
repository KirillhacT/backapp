from collections import defaultdict, Counter, OrderedDict, deque
from itertools import chain, cycle, accumulate
from pprint import pprint
import random

#setdefault() - создает ключ со значением, если таковой отсутствует, иначе возвращает значение
def one():
    table = {"Hydrogen": 1}
    print(table.get("Hydrogen")) #get() - возвращает значение по ключу, если нет то None
    table = table.setdefault("Carbon", 12)
    print(table)

#defaultdict() -> По умолчанию будет выставлен результат функции
def two():
    period_table = defaultdict(lambda: f"No idea")
    print(period_table["Egot"])

#Example
def three():
    food_counter = defaultdict(int)
    for food in ['spam', 'spam', 'eggs', 'shayrma']:
        food_counter[food] += 1
    print(food_counter)

#Counter - подчитывает кол-во элементов последовательности
def four():
    breakfast = ['spam', 'spam', 'eggs', 'shayrma']
    print(count := Counter(breakfast))

#OrderedList() - запоминает порядок, в котором добавлялись ключи,
# и возвращает их в том же порядке
def five():
    quotes = OrderedDict([
        ("One", 1),
        ("Two", 2),
        ("Three", 3),
        ("Four", 4),
    ])
    for quote in quotes:
        print(quote, quotes[quote])
#Deque
def six():
    word = "abba"
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


#Itertools
def seven():
    #chain() проходит по своим аргументам, как если бы они были единым
    #итерабельным объектом:
    for i in chain([1, 2], [1, 3]):
        print(i)

    # cycle() - бесконечная последовательность
    count = 0
    for item in cycle([1, 2]):
        # print(item)
        break

    #accumulate() - считает сумму последовательности
    mas = [1, 2, 3, 4]
    new_mas = []
    for item in accumulate(mas):
        new_mas.append(item)
    print(new_mas)
# seven()

#pprint - красивая распечатка данных на экран
def eight():

    quotes = OrderedDict([
       ('Moe', 'A wise guy, huh?'),
        ('Larry', 'Ow!'),
        ('Curly', 'Nyuk nyuk!'),
        ])
    pprint(quotes)
# eight()

#random
def nine():
    #choice - выбор
    print(random.choice([1, 2, 3, 4, 5]))
    #randint - рандомное число в заданном диапазоне
    print(random.randint(100, 200))
    #random - рандомное число от 0 до 1
    print(random.random())
nine()