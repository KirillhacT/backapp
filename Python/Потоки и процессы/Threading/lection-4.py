import time
import threading

def qw():
    def test():
        while True:
            print("test")
            time.sleep(1)

    thr = threading.Timer(5, test)
    thr.start()

    for _ in range(3):
        print("111")
        time.sleep(1)
    #Отменяет поток до его выполнения
    thr.cancel()
# qw()

data = threading.local()


# def t1():
#     data.value = {"value": 111}
#     print(data.value)
#
# def t2():
#     data.test = 222
#     print(data.test)

def get_name():
    print(data.name)

def t1():
    data.name = threading.currentThread().name
    get_name()

def t2():
    data.name = threading.currentThread().name
    get_name()

threading.Thread(target=t1).start()
threading.Thread(target=t2).start()