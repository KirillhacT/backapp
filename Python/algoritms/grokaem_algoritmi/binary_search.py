def binary_search(array: list, guess):
    count = 1
    low = 0
    high = len(array)-1
    while low <= high:
        middle = (low + high) // 2
        current = array[middle]
        print(current)
        count += 1
        if current == guess:
            return (current, count)
        if current < guess:
            low = middle + 1
        else:
            high = middle - 1
    return None
a = 452
b = [i for i in range(10000)]
result = binary_search(b, a)
if result == None:
    print("Ошибка")
else:
    print(result)
