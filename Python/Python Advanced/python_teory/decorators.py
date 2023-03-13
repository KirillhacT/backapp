def header(func):
    def inner(*args, **kwargs):    
        print("<h1>")
        func(*args, **kwargs)
        print("<h1/>")
    return inner

# def table(func):
#     def inner(*args, **kwargs):    
#         print("<table>")
#         func(*args, **kwargs)
#         print("<table/>")
#     return inner

#Можно навешивать несколько декораторов
#@table #say = table(header(say))
@header #say = header(say)
def say(name, count):
    print(f"hello, {name}, {count}")

# say = table(header(say))
# say("Vasya", 1)
say("Egor", 1)

#Example
from functools import wraps

count = {}

def counter(func):
    count[func.__name__] = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"функция {func.__name__} вызвана")
        count[func.__name__] += 1
        func(*args, **kwargs)

    return wrapper

def dealer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызвана до вызова функции {func.__name__}")
        func(*args, **kwargs)
        print(f"Вызвана после вызова функции {func.__name__}")
    return wrapper

@dealer
@counter
def first():
    pass

@dealer
@counter
def second():
    pass

first = dealer(counter(first))
first()

print(count)




        