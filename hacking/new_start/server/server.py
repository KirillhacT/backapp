import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создаем TCP - сокет
sock.bind(('localhost', 3030)) # Привязываем серверный сокет к localhost и 3030 порту

sock.listen(1) # Прослушиваем входящее соединение
conn, addr = sock.accept() # Метод который принимает входящее соединение.
while True:
    data = conn.recv(1024) # Получаем данные из сокета.
    if not data:
        break
    clear_data = data.decode("utf-8")
    conn.sendall(f"new_[{clear_data}]".encode("utf-8")) # Отправляем данные в сокет.
    print(data.decode("utf-8"))
conn.close()