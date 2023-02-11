import threading
import time

def get_data(data):
    #Текущий поток
    while True:
        print(f"[{threading.currentThread().name} - {data}]")
        time.sleep(5)

thr = threading.Thread(target=get_data, args=(str(time.time()),), name="thr-1") #Запятая для кортежа
# thr.start()


#Поток работает независимо от программы
# for i in range(100):
#     print(f"current: {i}")
#     time.sleep(1)
#     if i % 10 == 0:
#         #Кол-во активных потоков
#         print(f"active thread: {threading.activeCount()}")
#         #Список всех запущенных потоков
#         print(f"enumerate: {threading.enumerate()}")
#         #Показывает, работает ли текущий поток
#         print(f"thr-1 is alive: {thr.is_alive()}")

#Основной поток и изменение его имени
# print(threading.main_thread().name)
# threading.main_thread().setName("result")
# print(threading.main_thread().name)

def thread_data(data, value):
    for _ in range(value):
        print(f"[{threading.currentThread().name} - {data}]")
        time.sleep(1)

thr_list = []
for i in range(4):
    #1 поток выполнится 1 раз 2 - 2 раза, 3 - 3 раза
    thr = threading.Thread(target=thread_data, args=(str(time.time()), i), name=f"thr={i}")
    thr_list.append(thr)
    thr.start()

for i in thr_list:
    i.join()
print("finish")

