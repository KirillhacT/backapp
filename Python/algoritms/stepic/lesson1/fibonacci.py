from functools import lru_cache
import time
from matplotlib import pyplot as pl

def timed(func, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        func(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc




def fib1(n):
    #assert - проверка на истинность, если ложно выдает ошибку
    assert n >= 0
    return n if n <= 1 else fib1(n-1) + fib1(n-2)

# fib1 = lru_cache(maxsize=None)(fib1)
# print(fib1(100))
# аналог на lru_cache


cache = {}
def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n-1) + fib2(n-2)
    return cache[n]
# print(fib2(int(input())))
# можно переписать под декораторы

def memo1(func):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return inner
# fib1 = memo1(fib1)
# print(fib1(200))

def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


# def compare(functions, args):
#     for func in functions:
#         pl.plot(args, [timed(func, arg) for arg in args], label=func.__name__)
#     pl.legend()
#     pl.grid(True)
# compare([fib1, fib3], list(range(100)))








