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



        