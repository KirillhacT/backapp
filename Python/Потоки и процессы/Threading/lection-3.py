import time
import threading

value = 0
locker = threading.Lock()
# locker2 = threading.RLock()
#RLock отличается от Lock тем, что только исходный поток может разблокировать область

#Locker - блокирует поток до тех пор, пока предыдущие потоки не совершат работу
#тем самым синхронизирует его
def inc_value():
    global value
    while True:
        #Эквивалент
        with locker:
            value += 1
            time.sleep(0.5)
            print(value)
        # locker.acquire()
        # value += 1
        # time.sleep(0.5)
        # print(value)
        # locker.release()

for _ in range(5):
    threading.Thread(target=inc_value).start()
