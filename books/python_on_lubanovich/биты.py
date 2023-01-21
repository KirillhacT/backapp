import struct
import binascii

def bytes_and_bytesarray():
    blist = [1, 2, 3, 4, 255]
    the_bytes = bytes(blist)
    #Изменить массив байтов мы не можем
    print(the_bytes)

    the_bytes_list = bytearray(blist)
    print(the_bytes_list)
    the_bytes_list[1] = 13
    print(the_bytes_list)
    #Значение изменилось
# bytes_and_bytesarray()

# print(bytes(range(0, 256))) #Представление элементов от 0 до 255

def get_png_data():
    valid_png_header = b'\x89PNG\r\n\x1a\n' #Валидный PNG заголовок
    data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
        b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
    if data[:8] == valid_png_header:
        width, height = struct.unpack(">LL", data[16:24])
        print(width, height)
    else:
        print("Not valid")
    #pack() Обратный эффект - преобразует число в последовательность байт
    print(struct.pack(">L", 154))
# get_png_data()

#Библиотеки для работы с бинарными данными
# bitstring (http://bit.ly/py-bitstring);
# construct (http://bit.ly/py-construct);
# hachoir (https://pypi.org/project/hachoir);
# binio (http://spika.net/py/binio/);
# Kaitai Struct (http://kaitai.io/).

def binasci():
    #Преобразуем байты в строку и строку в байты
    valid_png_header = b'\x89PNG\r\n\x1a\n'
    print(binascii.hexlify(valid_png_header))
    print(binascii.unhexlify(b'89504e470d0a1a0a'))

# binasci()

def example2():
    str = '47494638396101000100800000000000ffffff21f9' + \
    '0401000000002c000000000100010000020144003b'
    gif = binascii.unhexlify(str)
    # print(gif)

    if gif[:6].decode("utf-8") == "GIF89a":
        print("Корректен")
example2()
