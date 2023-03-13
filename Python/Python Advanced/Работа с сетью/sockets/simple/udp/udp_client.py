import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    message = "Salam".encode("utf-8")
    sock.sendto(message, ("127.0.0.1", 8888))