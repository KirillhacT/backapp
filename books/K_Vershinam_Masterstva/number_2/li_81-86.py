from array import array
from random import random

fruits = ['grape', 'raspberry', 'apple', 'banana']

#sorted - возвращает отсортированную итерируемую последовательность в качестве нового объекта
#sort - сортирует сам исходную последовательность, поэтому в качестве своей работы возвращает None

new_fruicts = sorted(fruits, key=len, reverse=True)
#reverse - обратный порядок, key - по какому критерию проводится сортировка
print(new_fruicts, fruits.sort())

#Создание, сохранение и загрузка большого массива данных

#array - хранит в себе значения в виде байтов
#флаг d - двойная точность
floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])

fp = open("floats.bin", "wb")
floats.tofile(fp) #Сохраняем массив с данными в файле
fp.close()

floats2 = array("d")
fp = open('floats.bin', "rb")
floats2.fromfile(fp, 10**7) #Читаем 10 миллионов чисел из файла и записываем их в пустой массив
fp.close()

# print(floats2[-1])
print(floats2 == floats)

#Сортировка массива функцией sorted
a = array("d", [3, 2, 1])
a = array(a.typecode, sorted(a))
print(a)

