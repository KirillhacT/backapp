import random
from multiprocessing import Process, Event
import time


def test(event: Event):
    while True:
        event.wait()
        print("test")
        time.sleep(1)

def test_event(event: Event):
    while True:
        time.sleep(5)
        event.set()
        print("Event True")
        time.sleep(5)
        event.clear()
        print("Event False")


if __name__ == '__main__':
    event = Event()
    Process(target=test, args=(event,)).start()
    Process(target=test_event, args=(event,)).start()