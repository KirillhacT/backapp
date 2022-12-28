import base64

def example():
    str = input()
    encoded_str1 = str.encode() #Превращаем в байты
    print(encoded_str1)

    encoded = base64.b64encode(encoded_str1) #Кодируем в байтах
    print(encoded)

    encoded_str2 = base64.b64decode(encoded)# возвращаем в исходник в байтах
    print(encoded_str2)

    decoded = encoded_str2.decode() #Декодируем из байтов
    print(decoded)


