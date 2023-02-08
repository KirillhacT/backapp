def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    else:
        mas = signature + [0] * (n - 3)
        for i in range(3, n):
            mas[i] = mas[i-1] + mas[i-2] + mas[i-3]
        return mas
print(tribonacci([1, 1, 1], 13))

