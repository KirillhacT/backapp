import multiprocessing
import time
from multiprocessing import Process, Barrier, Lock

def func(barrier: Barrier, locker):
    name = multiprocessing.current_process().name
    #Пока в барьер стучится кол-во процессов, меньше заданного, он их не пропустит
    #Проблема решается увеличением входящих процессов
    print(f"[{name}] - спит 3 секунды")
    time.sleep(3)
    barrier.wait()
    print(f"[{name}] - запущено")

if __name__ == '__main__':
    barrier = Barrier(5)
    locker = Lock()
    for i in range(6):
        Process(target=func, args=(barrier, locker), name=f"pr-{i}").start()
