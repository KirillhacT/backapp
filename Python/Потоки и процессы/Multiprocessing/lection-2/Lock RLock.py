import multiprocessing
from multiprocessing import RLock
import time

#Lock - может заблокировать и разблокировать любой поток
#RLock - может разблокировать только из того потока, который и заблокировал
def get_value(l: RLock):
    #Краткая запись
    with l:
    # l.acquire()
        pr_name = multiprocessing.current_process().name
        print(f"Процесс [{pr_name}] запущен")
        time.sleep(5)
        print(f"Процесс [{pr_name}] выполнен")
    # l.release()


if __name__ == '__main__':
    lock = RLock()
    multiprocessing.Process(target=get_value, args=(lock,)).start()
    multiprocessing.Process(target=get_value, args=(lock,)).start()


