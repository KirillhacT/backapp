import os

with open("test.txt", "w") as file:
    file.write("Hello world\nShalom")

with open("test.txt") as file:
    text = ""
    flag = True
    while flag:
        line = file.readline()
        if not line:
            flag = False
            continue
        text += line
    print(text)

#Проверит файл на существование
print(os.path.exists("test.txt"))

#Проверка на файл или на директорию
print(os.path.isfile("test.txt"), os.path.isdir("test.txt"))

#Перемеиновываем файл
os.rename("test.txt", "test2.txt")

#Изменяем разрешения функцией chmod
# os.chmod("test2.txt", 0o400)

#Удаляем файл
# os.remove("test2.txt")

#Создаем директорию
if os.path.exists("Crow"):
    pass
else:
    os.mkdir("Crow")

#Создаем подкатегорию
if os.path.exists("Crow/Dawn_crow"):
    pass
else:
    os.mkdir("Crow/Dawn_crow")

#Удаляем диреторию
# os.rmdir("Crow")
# os.path.exists("Crow")

#Выводим на экран содержимое директории
print(os.listdir("Crow"))

#Получаем абсолютный путь и присоединяем два пути
# print(os.path.abspath("Crow"))
dir = os.path.abspath("Crow")
print(os.path.join(dir, "Zaid"))



