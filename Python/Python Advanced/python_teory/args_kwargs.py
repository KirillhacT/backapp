def example_args(*args):
    # print(args)
    print(args[2])

example_args("gh", [], {"a": 1})

def example_kwargs(**kwargs):
    # print(kwargs)
    # for i, j in kwargs.items():
    #     print(i, j)
    for i in kwargs:
        print(i, kwargs[i])
a = b = c = 0
example_kwargs(a=1, b=2, c=3)

# def quick_sort(A):
#     if len(A) < 2:
#         return A
#     N = len(A) // 2
#     middle = A[N]
#     mas = A[0:N] + A[N+1:]
#     down = [i for i in mas if i <= middle]
#     high = [i for i in mas if i > middle]
#     return quick_sort(down) + [middle] + quick_sort(high)
#
# print(quick_sort([3, 2, 1, 5, 1, 7, 9, 5, 4]))


















