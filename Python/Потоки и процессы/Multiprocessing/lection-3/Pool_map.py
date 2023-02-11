import multiprocessing
import random

"""Pool - позволяет выполнять нужные нам задания 
полностью параллельно, тем самым это также ускоряет
 нашу программу."""

def end_func(responce):
    print("Задание завершено!")
    print(responce)

def get_value(value):
    name = multiprocessing.current_process().name
    print(f"[{name}] value: {value}")
    return value

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as pool:
        # pool.map(get_value, list(range(100)))
        pool.map_async(get_value, list(range(100, 0, -1)), callback=end_func)
        pool.close()
        pool.join()

