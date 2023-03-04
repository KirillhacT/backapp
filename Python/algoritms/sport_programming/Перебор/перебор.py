n = 6 #Кол-во чисел (кол-во рекурсивных вызовов)
m = 1 #Идем до трех (глубина рекурсивных вызовов)
# a = [0]*n

def rec(idx, a=""):
    if idx == n:
        print(a)
        return
    for i in range(0, m + 1):
        # a[idx] = i
        rec(idx + 1, a + f'{str(i)} ')
rec(0)