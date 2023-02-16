import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("localhost", 3030))
sock.sendall("Hello world!".encode("utf-8"))
responce = sock.recv(1024)
clear_responce = responce.decode("utf-8")
print(clear_responce)
sock.close()