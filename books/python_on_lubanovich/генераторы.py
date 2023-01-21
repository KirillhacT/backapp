# def print_data(data, *, start=0):
#     print(data, start)
#
# data = ['a', 'b', 'c', 'd', "e"]
# print_data(data)

#Генератор
# def generators(*, first=0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# ranger = generators()
# for x in ranger:
#     print(x, end="  ")
# print()


#Включение генераторов
# f = (i for i in range(10))
# print(f)


def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            #flatten(item) - возвращает генератор со значениями, по которому мы пробегаемся в цикле
            # for subitem in flatten(item):
            #     yield item
            yield from flatten(item)
        else:
            yield item

lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(list(flatten(lol)))


