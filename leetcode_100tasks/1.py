#Палиндром число (divmod)
import bisect

x = 456
if x < 0:
    print("Число не палиндром, потому что оно отрицательное")
orig = x
new = 0
while x:
    digit = x % 10
    x //= 10
    # x, digit = divmod(x, 10) #Эквивалент
    new = new * 10 + digit
    """0 * 10 + 6 = 6
    6 * 10 + 5 = 65
    65 * 10 + 4 = 654
    """
# print(new)


#set() - hash
a = [1, 2, 3, 1]
# print(len(a) != len(set(a))) #Определяем, встречается ли дубликат числа в массиве


#Linked List - СЛОЖНАААА


#bitmask
a1 = 3
b = a1 & 1 #Возвращает последнюю битовую цифру числа a % 2
a1 >>= 1 #Битовый сдвиг на один элемент влево - (1.1) a //= 1 * 10
# print(a, b)


#Удаление из емайла ненужных элементов
#Множество емайлов можно засунуть в set() для кол-ва уникальных
email = "test.email+alex@leetcode.com"
name, dom = email.split("@")
name = name.split("+")[0] #test.email
name = name.replace(".", "") #testemail
# print(f"{name}@{dom}")


#slinding window
#Перебор всех массивов неуместен (скорость N^2)
# q = deque([]) можно использовать двустороннюю очередь в качестве подмассива
nums = [1, 2, 3, 4, 5]; k = 1
ans = float('-inf') #-бесконечность
cnt = 0 #Счетчик, оповещающий что мы достигли элемента k
cur = 0 #Текущая сумма
for i in range(len(nums)):
    cur += nums[i]
    cnt += 1
    if cnt == k:
        ans = max(ans, cur/k)
    elif cnt > k:
        cur -= nums[i-k]
        ans = max(ans, cur/k)
# print(ans)


#two pointers
#Решаем задачу о переставлении нулей в конец списка с помощью двух указателей
a = [0, 1, 2, 0, 3, 4]
j = 0
for i in range(len(a)):
    if a[i] != 0:
        a[i], a[j] = a[j], a[i]
        j += 1
# print(a)


#binary_searchif - проверяем, является ли число квадратом
#В данном случае мы перебираем бин поиском числа, которые могли бы быть квадратом нашего числа
num = 16
l, r = 1, num // 2 #от 1 до 8
while l <= r:
    mid = (l + r) // 2
    sq = mid * mid
    if sq == num:
        pass
        # print("yes")
    if sq < num:
        l = mid + 1
    else:
        r = mid - 1

#divmod
#Пытаемся сделать из числа однозначное, используя divmod с повтором
num = 10
while num >= 10:
    cur = num
    new_num = 0
    while cur:
        new_num += cur % 10
        cur //= 10
    num = new_num
# print(num)

#string
s = "PPALLP"
# return s.count("A") < 2 and s.count("LLL") == 0
#count - наше все


#Binary Tree - СЛОЖНАА


#stack проверяем на соответствие строки шаблону
s1 = "abc"
t1 = "ahbgdc"
stack = list(s1)[::-1] #cba

for c in t1:
    if stack and stack[-1] == c:
        stack.pop() #cba cb c; так как and ленивый, мы не возьмем элемент из пустого массива
# print(len(stack) == 0)

#binary tree - ну такое


#divmod Прибавление еденицы к массиву
carry = 1
digits = [1, 2, 3]
for i in range(len(digits)-1, -1, -1):
    carry, digits[i] = divmod(digits[i]+carry, 10)
digits = digits if not carry else [carry] + digits
# print(digits)

#sorting - meeting rooms (заблокировано)
intervals = [[7, 10], [2, 4]]
intervals.sort()
for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[i-1][1]:
        print("No")
        exit()
# print("Yes")


#Linked List - ...


#hash Проверка, есть ли в два числа в массиве такие, что произведение одного из них на 2 равно другому
# arr = [0, 0]
# hash = {}
# count_0 = 0
# for i, j in enumerate(arr):
#     if j == 0:
#         count_0 += 1
#         if count_0 == 2:
#             print("Yes")
#     hash[j] = i
# for i in hash:
#     cur_num = i * 2
#     if cur_num in hash and cur_num != 0:
#         print(cur_num)
#         print("Yes")
# print("No")
hash = set()
arr = [10,2,5,3]
for num in arr:
    if num * 2 in hash or num / 2 in hash:
        pass
        # print("Yes")
        # exit()
    hash.add(num)
# print("No")


#dp - Tribonacci
n = 4
T = [0, 1, 1] + [0] * (n - 2)
for i in range(3, n + 1):
    T[i] = T[i-1] + T[i-2] + T[i-3]
# print(T)


#dp - Треугольник паскаля
n = 5
dp = [[1], [1, 1]] #[1, 2, 1]
if n < 3:
    print(dp[:n])
for _ in range(n-2):
    len_cur_row = len(dp[-1])
    next_row = [1] + [0] * len_cur_row #[1, 0, 0] [1, 0, 0, 0]
    for i in range(1, len_cur_row):
        #от 1 до длины последнего (2) (3)
        # next_row.append(dp[-1][i] + dp[-1][i-1])
        next_row[i] = dp[-1][i] + dp[-1][i - 1]
        #1 + 1 -> 2; 1 + 2 -> 3, 2 + 1 -> 3
    next_row[-1] = 1
    dp.append(next_row)
# print(dp)
#Треугольник паскаля 2, находим ряд чисел по индексу
# mas = [[1], [1, 1]]
# rowIndex = 5
# if rowIndex < 2:
#     print(mas[rowIndex])
#     exit()
# for _ in range(1, rowIndex):
#     cur_row = [1]
#     for i in range(1, len(mas[-1])):
#         cur_row.append(mas[-1][i] + mas[-1][i-1])
#     cur_row += [1]
#     mas.append(cur_row)
# print(mas[rowIndex])


#bitmask - вывести число, единожды встречающееся в массиве
a = [4,1,2,1,2]
cur = 0
for i in a:
    cur ^= i
    # print(cur)

#binary_search - находим гору в массиве
#Заметка по bin поиску, если условие не проходит, то можно
#Сделать проверку границ нестрогой, убрать единицы при делении пополам, возвращаем либо правую либо левую границу
arr = [0,10,5,2]
l, r = 0, len(arr)-1
while l <= r:
    mid = (l + r) // 2
    if arr[mid - 1] < arr[mid] > arr[mid + 1]:
        break
        # print(mid)
        # exit()
    if arr[mid - 1] < arr[mid] < arr[mid + 1]:
        l = mid
    else:
        r = mid


#string вычисляем корректный палиндром без учета знаков и цифр
s = "A man, a plan, a canal: Panama"
l, r = 0, len(s) - 1
while l <= r:
    if not s[l].isalnum():
        l += 1
        continue
    if not s[r].isalnum():
        r -= 1
        continue
    if s[l].lower() != s[r].lower():
        break
        # print("No")
        # exit()
    l += 1
    r -= 1
# print("True")

#string - переворот массива строк

s = ["h", "e", "l", "l", "o", "f"]
i = 0
j = len(s) - 1
while i <= j:
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1
# print(s)

#binary search - поиск квадрата числа или ближайшего к нему
if x < 2:
    pass
    # print(x)
l, r = 0, x // 2
while l <= r:
    mid_number = (l + r) // 2
    if mid_number * mid_number == x:
        pass
        # print(mid_number)
    if mid_number * mid_number < x:
        l = mid_number + 1
    else:
        r = mid_number - 1
# print(r) #Строго возвращаем правую границу

#hash - вычисляем букву, добавленную в строку в произвольном месте
from collections import Counter
strq = "a"
tq = "aa"
# print(list((Counter(tq) - Counter(strq)).elements())[0])


#stack - удаляем зеркально повторяющиеся числа
s = "aababaab"
s1 = "azxxzy"
stack = list()
for i in s1:
    if stack:
        if stack[-1] == i:
            stack.pop()
            continue
    stack.append(i)
# print(stack)


#Two pointers - Переворот каждого слова в предложении
s = "Egor Egor"
# new_s = " ".join([i[::-1] for i in s.split(" ")])
# print(new_s)
words = s.split(" ")
for index, word in enumerate(words):
    i = len(word) - 1
    new_str = ""
    while i >= 0:
        # word[i], word[j] = word[j], word[i]
        new_str += word[i]
        i -= 1
    words[index] = new_str
# print(words)


#binary search - ищем в массиве чисел позицию заданного числа
nums = [1, 3, 5, 6]
target = 5
result = bisect.bisect_left(nums, target)
# print(result)


#math - определяем, является ли число n степенью числа k
n = 625
k = 5
while n != 1:
    if n < 1:
        pass
        # print("No")
        # exit()
    n /= k
# print("Yes")
#Реализация рекурсией
def isPowerNumber(n, p) -> bool:
    if n < 1:
        return False
    if n == 1:
        return True
    return isPowerNumber(n / p, p)
# print(isPowerNumber(16, 4))


#hash
"""Если задачу можно решить с помощью словаря, то проще ее можно 
   решить с помощью коллекции Counter"""
s = "anagram"
t = "nagaram"
c1 = Counter(s)
t1 = Counter(t)
# print(c1 == t1)


#array - вычисляем, можем ли мы поставить в массив нек. кол-во единиц так, чтобы они повторялись через 1
flowerbed = [1, 0, 0, 0, 1]
flowerbed = [0] + flowerbed + [0]
n = 1
for i in range(1, len(flowerbed)-1):
    if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
        flowerbed[i] = 1
        n -= 1
# print(n <= 0)


#Binary Tree


#stack проверяем две строки на равенство с учетом символа стирания - решетки
s = "ab#c"
t = "ad#c"
def typing(s):
    stack = []
    for i in s:
        if i == "#":
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return "".join(stack)
print(typing(s) == typing(t))


#Linked List


#math является ли число степенью двойки
n = 16
if n == 0:
    pass
    # print("No")
    # exit()
while n % 2 == 0:
    n //= 2
# print(n == 1)


#Linked List


#bitwice
x = 1
y = 4
ans = 0
while x or y:
    ans += (x & 1) != (y & 1)
    x >>= 1
    y >>= 1
# print(ans)

nums = [9,6,4,2,3,5,7,0,1]
ran = set(range(len(nums)+1))
# print(ran)
st = ran - set(nums)
print(list(st)[0])


































