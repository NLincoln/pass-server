import socket


class Server:
    def __init__(self, bind_options=('127.0.0.1', 8888)):
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind(bind_options)
        self.listen_socket.listen(1)

    def handle_request(self, callback):
        client_connection, client_address = self.listen_socket.accept()
        request = client_connection.recv(1024)
        response = callback(request)

        client_connection.sendall(bytes(response, 'utf8'))
        client_connection.close()
