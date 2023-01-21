import unicodedata


def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value) #Преобразует значение в имя в аски коде
    value2 = unicodedata.lookup(name) #Восстанавливает значение по названию
    print(f'value="{value}", name="{name}", value2="{value2}"')

# unicode_test("\u4235")

# print("plac\u00e9") #вставка символа из юникода
# print("caf\N{LATIN SMALL LETTER E WITH ACUTE}") #вставка символа из юникода c помощью имени
# print(chr(233)) #Преобразование числа в символ
# print(ord("A")) #Преобразование символа в строку

#Кодируем строку
def endecode():
    snowman = "\u2603"
    # print(snowman)
    ds = snowman.encode("utf-8")
    print(ds, len(ds))
    ds2 = ds.decode("utf-8")
    print(ds2)
# endecode()

def normalize():
    eacute = 'é'
    #Создаем е с загутком разными способами
    eacute_combined1 = "e\u0301"
    eacute_combined2 = "e" + "\u0301"
    eacute_combined3 = "e\N{COMBINING ACUTE ACCENT}"
    print(eacute_combined1, eacute_combined2, eacute_combined3)

    #Несмотря на то, что символы выглядят аналогично, они являются различными
    print(eacute == eacute_combined1)

    #Нормализуем значение с помощью функции normalize()
    eacute_normalize = unicodedata.normalize("NFC", eacute_combined1)
    #Теперь они равны
    print(eacute == eacute_normalize)
# normalize()

def example1():
    mystery = "\U0001f4a9"
    mystery2 = "💩"
    # print(mystery)
    # print(name := unicodedata.name(mystery))
    pop_bytes = mystery.encode("utf-8")
    print(pop_bytes)
    # print(pop_bytes)
    pop_string = pop_bytes.decode("utf-8")
    print(pop_string)
    print(pop_string == mystery2)

example1()
