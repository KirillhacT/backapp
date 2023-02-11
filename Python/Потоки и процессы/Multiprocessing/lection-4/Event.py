import random
from multiprocessing import Process, Event
import time




def test(event: Event):
    for i in range(20):
        if i % 5 == 0:
            event.set()
        else:
            event.clear()
        event.wait()
        print(f"test-{i}")
        time.sleep(1)

if __name__ == '__main__':
    event = Event()
    Process(target=test, args=(event,)).start()