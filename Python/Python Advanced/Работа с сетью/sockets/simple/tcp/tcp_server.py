import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080)) #Резервируем порт и айпи
sock.listen(5) #Сколько клиентов могут за раз подключиться
# sock.setblocking(True) #Устанавливаем блокирующий режим/отключаем
sock.settimeout(5) #Ставит тайм аут ожидания запроса

while True:
    try:
        client, addr = sock.accept() #Принимаем клиента
    # except socket.error:
    #     print(f"\rno clients", end="")
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print(f"Message {result.decode('utf-8')}")
