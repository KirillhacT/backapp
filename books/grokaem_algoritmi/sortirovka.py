def bubble_sort(array: list):
    N = len(array)
    for i in range(N-1):
        for j in range(N-1-i):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]

# a = [5, 1, 2, 4, 9]
# bubble_sort(a)
# print(a)

def vstavka(array: list):
    newArr = []
    for i in range(len(array)):
        smallest = array[0]
        smallest_index = 0
        for j in range(1, len(array)):
            if array[j] < smallest:
                smallest = array[j]
                smallest_index = j
        newArr.append(array.pop(smallest_index))
    print(newArr)
# a = [5, 4, 3, 2, 1]
# vstavka(a)

def quick_sort(array: list):
    if len(array) < 2:
        return array
    N = len(array) // 2
    pivot = array[N]
    mas = array[:N] + array[N+1:]
    # a = [1, 2, 3, 4, 5]
    # x = 2 - индекс нужного элемента
    # b = a[:x] + a[x+1:]
    # print(b) - список без выбранного элемента
    # [1, 2, 4, 5]
    less = [i for i in mas if i <= pivot]
    greater = [i for i in mas if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([5, 1, 2, 6, 7, 5, 1, 9, 0, 42]))
