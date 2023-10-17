import logging
import socket

logging.basicConfig(level=logging.INFO)


class Api:
    """Represents a simple web API."""

    def __init__(self):
        """Initialise the API."""
        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )
        self.running = True

    def run(self, host: str, port: int):
        """Start listening for connections."""
        self.server_socket.bind((host, port))

        logging.info(f"Listening on {host}:{port}")

        self.server_socket.listen(1)

        while self.running:
            client_socket, address = self.server_socket.accept()
            logging.info(f"Connection from {address}")

            request_data = client_socket.recv(1024)
            logging.info(f"Request data: {request_data.decode('utf-8')}")

            response_data = "HTTP/1.1 200 OK\n\nHello, World!"

            client_socket.sendall(response_data.encode("utf-8"))
            client_socket.close()
