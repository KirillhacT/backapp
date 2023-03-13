import socketserver

class EchoUPDHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data, socket = self.request
        print(f"Addres: {self.client_address[0]}")
        print(f"Data: {data.decode()}")
        socket.sendto(data, self.client_address)

if __name__ == '__main__':
    with socketserver.UDPServer(("", 8888), EchoUPDHandler) as server:
        server.serve_forever()