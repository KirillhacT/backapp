import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto("Class udp sock".encode("utf-8"), ("127.0.0.1", 8888))