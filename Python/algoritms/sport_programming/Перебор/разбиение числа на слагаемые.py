n = 3
a = [0] * n


def rec(ind=0, sum=0, last=1):
    if sum == n:
        print(n, '=', sep='', end='')
        print(a[:ind])
        return
    for i in range(last, n - sum + 1):
        a[ind] = i
        rec(ind + 1, sum + i, i)

rec()