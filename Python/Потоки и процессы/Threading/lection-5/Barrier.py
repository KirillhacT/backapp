import time
import threading
import random

def test(barrier):
    #Барьер будет ожидать, пока не выполнится определенное число потоков до того, чтобы продолжить дальше
    time.sleep(random.randint(10, 15))
    print(f"{threading.currentThread().name} запущен", end="\n")
    barrier.wait()
    print(f"{threading.currentThread().name} преодолел барьер", end="\n")

bar = threading.Barrier(5)
for i in range(10):
    threading.Thread(target=test, args=(bar,), name=f"thr-{i}").start()