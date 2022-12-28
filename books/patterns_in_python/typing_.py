from typing import Optional, Union

#Аннотация
Vector = list[int] #Список интов
StringDict = dict[str, int]

def scale(vector: Vector, scalar: int) -> Vector:
    return [scalar * num for num in vector]

# new_vector = scale([1, 2, 3], 4)
# print(new_vector)

def print_dict(dictionary: StringDict) -> None:
    for key in dictionary:
        print(f"key = {key}, value = {dictionary[key]}", end="\n")

# print_dict({"Egot": 2, "Vanya": 11})

#Optional
"""Если вы пометите переменную типом int 
и попытаетесь присвоить ей None, будет ошибка
Для таких случаев предусмотрена в модуле typing аннотация 
Optional с указанием конкретного типа"""

def foo1(price: Optional[int] = None):
    print(price)
foo1()

#Union
"""Для случаев, когда необходимо допустить использование не
 любых типов, а только некоторых, можно использовать аннотацию 
 Union с указанием списка типов в квадратных скобках."""

def foo2(x: Union[float, int, complex]) -> int:
   return int(x)

print(foo2(5.12))
