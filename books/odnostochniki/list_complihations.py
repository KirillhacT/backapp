# list complihations


# 1) Список из кортежей с двумя переменными
a = [(x, y) for x in range(3) for y in range(3)]
# print(a)


dict = {
    "car": 3,
    "house": 2,
}

#2)dict.items - возвращает ключ значение от словаря
b = [(x, y) for x, y in dict.items()]
# print(b)

text = """There are many variations of passages 
of Lorem Ipsum available, but the majority have 
suffered alteration in some form, by injected 
humour, or randomised words which don't look 
even slightly believable. If you are going to 
use a passage of Lorem Ipsum, you need to be 
sure there isn't anything embarrassing hidden in
 the middle of text. All the Lorem Ipsum generators
 on the Internet tend to repeat predefined chunks as 
 necessary, making this the first true generator on 
 the Internet. It uses a dictionary of over 200 Latin 
 """
#3)разбиваем текст на строки, и проходим по каждой строке,
#выбирая слова, состоящие более чем из 3 букв

c = [[x for x in line.split(" ") if len(x) > 3] for line in text.split("\n")]
print(c)

x = {x: x**x for x in range(10)}
print(x)

