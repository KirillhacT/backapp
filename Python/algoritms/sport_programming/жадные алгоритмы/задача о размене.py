s = 37
a = [10, 5, 2, 1]
n = len(a)

cnt = 0
for i in range(n):
    cnt += s // a[i] #3 + 1 + 1
    s %= a[i] #37 % 10 = 7, 7 % 5 = 2, 2 % 2 = 0
print(cnt)