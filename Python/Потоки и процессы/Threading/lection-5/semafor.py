import time
from threading import Thread, BoundedSemaphore, currentThread, Lock

max_connections = 3
# POOL - семафор (допускает только определенное число потоков)
pool = BoundedSemaphore(value=max_connections)
locker = Lock()

def test():
   #Работа семафора и локера в стеке
    with pool:
        with locker:
            print(currentThread().name)
        time.sleep(3)

for i in range(10):
    Thread(target=test, name=f"thr-{i}").start()