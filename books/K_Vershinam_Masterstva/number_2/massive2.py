from collections import abc
from random import randint

# nums = ["1", "2", "3"]
# codes = [last := int(i) for i in nums]
# print(last, codes)


# symbols = [randint(1, 20) for i in range(10)]
# print(symbols)
# print(list(filter(lambda x: x > 10, symbols)))

# def fixed(value):
#     num = 1
#     try:
#         hash(value)
#     except TypeError:
#         num = 2
#         return False
#     finally:
#         print(num)
#     return True
# tf = (10, 'alpha', (1, 2, 3))
# tm = (10, 'alpha', [1, 2])
# print(fixed(tf), fixed(tm))


# l = (1, 2, 3)
# l1, l2, l3 = l

# a, b, *c = [i for i in range(5)]
# print(a, b, c)


# typ = (1, 2, 3)
# (_, _, x) = typ
# print(x)


# print([*range(4), 4])


# def strange_func(a, b, c, *args):
#     return a, b, c, args
# print(strange_func(*[1, 2], 3,*range(8, 10)))

# metro_areas = [
#   ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#   ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#   ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#   ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#   ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
# ]
# def main():
#     # for name, _, _, (lat, lon) in metro_areas:
#     #     if lon <= 0:
#     #         print(name, lat, lon)
#
#     for record in metro_areas:
#         # print(record)
#         match record:
#             case [name, _, _, (lat, lon)] if lon <= 0:
#                 print(name, lat, lon)
# main()

# board = [["_"] * 3 for i in range(3)]
# # print(board)
# board[1][1] = "X"
# board[2][1] = "O"
#
# board[0][2] = "X"
# board[2][0] = "O"
#
# board[2][2] = "X"
# board[1][2] = "O"
#
# board[0][0] = "X"
# print(*board, sep="\n")