import logging
import socket

from .request import Request, from_string
from .response import Response
from .router import RequestHandler, Router

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s [%(asctime)s] [%(name)s] %(message)s",
)


class Api:
    """Represents a simple web API."""

    def __init__(self):
        """Initialise the API."""
        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )
        self.running = True

        self.default_router = Router()

    def run(self, host: str, port: int):
        """Start listening for connections."""
        self.server_socket.bind((host, port))

        logging.info(f"Running on {host}:{port}")

        self.server_socket.listen(1)

        while self.running:
            client_socket, address = self.server_socket.accept()

            request: bytes = client_socket.recv(1024)
            response: bytes = self.handle_request_bytes(request)

            client_socket.sendall(response)
            client_socket.close()

    def handle_request_bytes(self, bytes: bytes) -> bytes:
        request = from_string(bytes.decode("utf-8"))
        response = self.handle_request(request)

        logging.info(f"{request.method} {request.path} - {response.status}")

        return f"HTTP/1.1 {response.status}\n\n{response.body}".encode("utf-8")

    def handle_request(self, request: Request) -> Response:
        """Handle a request."""
        handler: RequestHandler = self.default_router.find(request.path, request.method)
        response: Response = handler(request)

        return response
