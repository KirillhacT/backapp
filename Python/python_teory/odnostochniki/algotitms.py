#Анаграммы - слова, состоящие из одинаковых букв, но в разном порядке

is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)
print(is_anagram("lives", "elvis"))

#Палиндром - слово, читающиеся одинаково справа налево и слево направо
is_palindrom = lambda phrase: phrase.lower() == phrase[::-1].lower()
print(is_palindrom("rats live on no evil star"))

#Поиск факториала в одной строке
factorial = lambda x: factorial(x-1) * x if x > 1 else 1
print(factorial(5))

#Расстояние Левинштейна
ls = lambda a, b: len(b) if not a else len(a) if not b else min(
    ls(a[1:], b[1:])+(a[0] != b[0]),
    ls(a[1:], b)+1,
    ls(a, b[1:])+1,
)
print(ls("cat", "chello"))

