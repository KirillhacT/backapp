import sys

def get_square_perimeter(square_size):
    perimeter = square_size * 4
    return perimeter



if len(sys.argv) < 2:
    print("Введите сторону квадрата!")
    exit()

square_size = sys.argv[1]

if not square_size.isnumeric():
    print("Передайте число в качестве аргумента")
    exit()
square_size = int(square_size)
perimeter = get_square_perimeter(square_size=square_size)
print(f"Периметр квадрата со стороной {square_size} равен {perimeter}")

#Типы данных
set() #Множество
tuple() #Кортеж
list() #Список
dict() #Словарь

#Как обойти словарь
# dt = {
#     "name1": "egor",
#     "name2": "ivan",
#     "name3": "vlados"
# }
# for i in dt:
#     print(f"Ключ - {i} значение - {dt[i]}")
# #или
# for i, k in dt.items():
#     print(f"Ключ - {i} значение - {k}")