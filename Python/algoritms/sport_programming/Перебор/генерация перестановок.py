n = 4
a = [0]*n
used = [False] * (n + 1)

def rec(idx, a=""):
    if idx == n:
        print(a)
        return
    for i in range(1, n + 1):
        if used[i]:
            continue
        # a[idx] = i
        used[i] = True
        rec(idx + 1, a + f'{str(i)} ')
        used[i] = False
rec(0)