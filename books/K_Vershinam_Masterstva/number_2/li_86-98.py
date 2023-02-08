from array import array
import numpy as np
from collections import deque

"""
memoryview  – это тип последовательности в  общей памяти,
который позволяет работать со срезами массивов, ничего не копируя
"""

#встроенный класс memoryview --------------------------
def memoryviews():
    octets = array("B", range(6))
    m1 = memoryview(octets)
    print(m1.tolist())

    m2 = m1.cast("B", [3, 2])
    print(m2.tolist())

    m3 = m1.cast("B", [2, 3])
    print(m3.tolist())

    m2[1, 1] = 22
    m3[1, 1] = 33
    #Срез в памяти
    print(octets)
# memoryviews()


#Двусторонняя очередь
def deq():
    dq = deque(range(10), maxlen=10)
    #append - appendleft
    #pop - popleft
    #extend - extendleft
    print(dq); dq.rotate(3); print(dq)
    #dq.rotate - сместиться на 3 элемента
    dq.rotate(-3) #Возвращение в исходное состояние

    dq.appendleft(-1) #Добавление в левый край
    print(dq)
    dq.extend([11, 22, 33]) #Добавить несколько элементов
    print(dq)
    #Так как максимальная длина 10, то первые 2 элемента удалились
# deq()

#Аргумент key – истинный бриллиант
#Передается в функцию сравнения двух элементов
l = [1, 2, "3", "4", 3, 5, "6"]
print(sorted(l, key=int))