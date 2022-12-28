def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print(factorial(3))
# print(fibonacci(3))

def rec(n):
    print(n)
    if n == 5:
        return 
    rec(n+1)
    print("lol {}".format(n))
# rec(1)


def summa(N):
    if N == []:
        return 0
    return N[0] + summa(N[1:])
print(summa([4, 2, 1, 11]))