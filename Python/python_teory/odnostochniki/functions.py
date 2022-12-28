#lambda функция
a = lambda x, y: x ** y
print(a(2, 3))

#функция map
str = ["1", "2", "3"]
print(list(map(int, str)))

b = [
    "private 123",
    "23",
    "aboba 13"
]
mark = map(lambda s: (True, s) if "23" in s else (False, s), b)
print(list(mark))


#Срезы
# a = "hello world"
# print(a[4:])

#С помощью среза находим промежуток текста 15 на 15 символов
#в котором встречается нужное слово
#<str>.find() - возвращает индекс найденного элемента
text = """We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked."""

find = lambda text, word: text[text.find(word)-18:text.find(word)+18] if word in text else -1
print(find(text, "SQL"))


txt = [
    [1, 2, 3, "fail", 5], [10, 11, 12, "fail", 14], [20, 21, 22, "fail", 42]
]
sample = [list[2::] for list in txt]
new_sample = []
for i in sample:
    new_sample += i
new_sample[1::3] = new_sample[::3]
print(new_sample)

#Пример выражения генератора
# sum(x*x for x in range(20))

#Функция any() - работает как or, если есть одно истинное
#Функция all() - работает также, но вместо or применяем and
# print(any([True, False]))
# print(all([True, False]))

companies = {
    'CoolCompany': {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
    'CheapCompany': {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
    'SosoCompany': {'Esther' : 38, 'Cole' : 8, 'Paris' : 18},
}
# Полный проход по словарю
# for x in companies:
    # print(x) #Ключи
    # print(companies[x]) #Значения по ключу
    # print(companies[x].values()) #Значение прямо из объекта словаря
    # print(companies[x].keys()) #Ключи прямо из объекта словаря

illegal = [x for x in companies if any(y<9 for y in companies[x].values())]
print(illegal)

# функция zip()
# запаковывает итерируемые объекты в кортежи, исходя из их индексов
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
zipped = list(zip(list_1, list_2))
print(zipped)

#Распаковка назад, возвращает кортежи
list_1_new, list_2_new = zip(*zipped)
print(list_1_new, type(list_2_new))

column_names = ['name', 'solary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
    ('Bob', 99000, 'mid-level manager'),
    ('Frank', 87000, 'CEO')]
dp = [dict(zip(column_names, row)) for row in db_rows]
print(dp)

#Обращение списка - reverse
# a = [1, 2, 3]
# b = a[::-10.]
# print(b)

