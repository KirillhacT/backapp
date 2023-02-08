# from random import randint
#
# param = randint(0, 3)
#
# match param:
#     case 0:
#         print("NO")
#     case 1:
#         print("YE")
#     case 2:
#         print("Yes")
#     case 3:
#         print("YESSSS")


#match/case - оператор одновременно и сопоставления и распаковки
mas = [1, 2, 3, 4, 5, *[1, 2]]
# print(mas)
match mas:
    case [1, two, three, four, *five] if two == 2:  # Условие также учитывается
        print(two, three, four, five)
    case _:  # В любов другом случае
        raise SyntaxError("LOL")

