import multiprocessing
import random
import time


def add_value(locker, array, index):
    with locker:
        num = random.randint(0, 20)
        array[index] = num
        print(f"array[{index}] = {num}")
        time.sleep(1)


if __name__ == '__main__':
    arr = multiprocessing.Array("i", range(10))
    locker = multiprocessing.Lock()
    process = []

    for i in range(10):
        pr = multiprocessing.Process(target=add_value, args=(locker, arr, i,))
        process.append(pr)
        pr.start()
    for i in process:
        i.join()
    print(list(arr))

