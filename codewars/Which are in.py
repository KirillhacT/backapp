av = ["zone", "abigail", "theta", "forma", "libe", "zas"]
k = int(input())

n = len(av)
if n == 0 or k <= 0 or k > n:
    print(None)
else:
    max_len = 0
    max_num = ""
    for i in range(len(av)):
        if i > len(av) or k + i > len(av):
            break
        else:
            # current = "".join(av[i:k+i]) эквивалент в  строку
            current = ""
            for j in range(i, k+i):
               current += av[j]
            if len(current) > max_len:
                max_len = len(current)
                max_num = current
    print(max_len)
    print(max_num)