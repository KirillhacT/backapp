import os
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (w or not(x)) and (w != y) and (w <= z):
#                     if z != 0:
#                         print(x, y, z, w)

#8)
# a = int(input())
# b = int(input())
# c = int(input())

# count = 0
# massive = [a, b, c]
# for i in range(3):
#     if massive[i] % 3 == 0:
#         count += 1
# print(count)

#9)
# a = float(input())
# b = float(input())
# c = float(input())

# D = b**2 - 4 * a * c
# if D == 0:
#     x = -b / (2 * a)
#     print(f"Корень уравнения {x}")
# elif D < 0:
#     print("Корней нет!)")
# elif D > 0:
#     x1 = (-b + D ** 0.5) / (2 * a)
#     x2 = (-b - D ** 0.5) / (2 * a)
#     print(f"Корни уравнения {x1} и {x2}")


#10)
# first_side = int(input())
# second_side = int(input())
# third_side = int(input())

# if first_side == second_side == third_side:
#     print("1) Треугольник равносторонний")
# elif first_side == second_side or first_side == third_side or second_side == third_side:
#     print("1) Треугольник равнобедренный")
# else:
#     print("1) Треугольник разносторонний")

# theory_of_pifagor = lambda x, y, z: x**2 == y**2 + z**2 
# is_rectangular = any
# (
#     [
#         theory_of_pifagor(first_side, second_side, third_side), 
#         theory_of_pifagor(second_side, first_side, third_side), 
#         theory_of_pifagor(third_side, first_side, second_side)
#     ]
# )
# if is_rectangular:
#     print("2) Треугольник прямоугольный")
# else:
#     print("2) Треугольник не прямоугольный")
# if first_side + second_side > third_side or first_side + third_side > second_side or second_side + third_side > first_side:
#     print("3) Треугольник существует")
# else:
#     print("3) Треугольник не существует")

# print(os.path())

