import time
from multiprocessing import Process, Condition, Event

def f1(cond):
    while True:
        with cond:
            cond.wait()
            print("Получили событие")
def f2(cond):
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print(f"f2: {i}")
        time.sleep(1)

#Эквивалент на eventах
def q1(event):
    while True:
        event.wait()
        print("Получили событие")
        event.clear()

def q2(event):
    for i in range(100):
        if i % 10 == 0:
            event.set()
        else:
            print(f"f2: {i}")
        time.sleep(1)


if __name__ == '__main__':
    cond = Condition()
    event = Event()
    # Process(target=f1, args=(cond,)).start()
    # Process(target=f2, args=(cond,)).start()

    Process(target=q1, args=(event,)).start()
    Process(target=q2, args=(event,)).start()