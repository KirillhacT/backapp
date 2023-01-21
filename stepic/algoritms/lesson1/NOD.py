import random

def test(func, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert func(a, a) == func(a, 0) == a
        assert func(b, b) == func(b, 0) == b
        assert func(a, 1) == func(b, 1) == 1
    return "Все ок"

def NOD1(a, b):
    assert a >= 0 and b >= 0
    for i in reversed(range(max(a, b) + 1)):
        if i == 0 or a % i == b % i == 0:
            return i
# print(test(NOD1))

def NOD2(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)

def NOD3(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return NOD3(a % b, b)
    else:
        return NOD3(a, b % a)
print(NOD2(3123, 1233))
print(NOD3(734731112, 328478232))