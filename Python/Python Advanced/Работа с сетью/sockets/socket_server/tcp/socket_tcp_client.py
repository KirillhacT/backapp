import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("127.0.0.1", 8888))
    sock.send(b"Ky ky epta")
    result = sock.recv(64)
    print("Responce: ", result)