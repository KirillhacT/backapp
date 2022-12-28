# a = [4, 5, 6, 1, 2]
# #нужно найти макс. подмассив
# count = 1
# max_count = -1

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         count += 1
#     else:
#         count = 1
#     if max_count < count:
#             max_count = count
# print(max_count)


# def dasdas(massive: list):
#     m = []
#     for i in range(len(massive)):
#         current_sum = 1
#         for j in range(len(massive)):
#             if j == i:
#                 continue
#             else:
#                 current_sum *= massive[j]
#         m.append(current_sum)
#     return m
# print(dasdas([1, 2, 3, 4]))


# a = lambda n: n if n <= 1 else a(n-1) + a(n-2)
# print(a(10))

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(100))