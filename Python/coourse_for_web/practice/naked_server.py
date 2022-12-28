import socket

#Создаем сервер
server = socket.create_server(("127.0.0.1", 8000)) 
#Одно и тоже, только в более длинном виде
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("127.0.0.1", 8000))

#Для освобождения порта
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Длина очереди
server.listen(10)

try:
    while True:
        client_socket, address = server.accept()
        received_data = client_socket.recv(1024).decode("utf-8")

        # print("Получаем данные по сокету", received_data)

        path = received_data.split(" ")[1]
        responce = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" \
            f"Привет<br/>Path: {path}"

        #Выключение сокетов и закрытие сервера
        client_socket.send(responce.encode("utf-8"))
        client_socket.shutdown(socket.SHUT_RDWR)
except KeyboardInterrupt:
    server.shutdown(socket.SHUT_RDWR)
    server.close()




