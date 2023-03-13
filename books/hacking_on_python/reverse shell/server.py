import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(("127.0.0.1", 8888))
    sock.listen(5)

    client, addr = sock.accept()
    while True:
        command = str(input("Enter command: "))
        client.send(command.encode())
        if command.lower() == "exit":
            break
        result_output = client.recv(1024).decode("utf-8")
        print(result_output)
    client.close()
