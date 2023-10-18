import json
import logging
import socket

from .request import Request, from_string
from .response import Response
from .router import RequestHandler, Route, Router

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
        self.routers: dict[str, Router] = {}

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

        response_body_str: str = json.dumps(response.json)

        return f"HTTP/1.1 {response.status}\n\n{response_body_str}".encode("utf-8")

    def handle_request(self, request: Request) -> Response:
        """Handle a request by finding the appropriate request handler from all routers."""
        route: Route = (request.path, request.method)

        for path in self.routers:
            if not request.path.startswith(path):
                continue

            residual_path: str = request.path[len(path) :]
            subroute: Route = (residual_path, request.method)

            if subroute not in self.routers[path]:
                continue

            handler: RequestHandler = self.routers[path].find(subroute)
            return handler(request)

        handler: RequestHandler = self.default_router.find(route)
        return handler(request)

    def add_router(self, path: str, router: Router):
        """Add a router to the API at a certain path."""
        self.routers[path] = router

    def get(self, path: str):
        """A convenience decorator for adding GET routes to default router."""
        return self.default_router.get(path)

    def put(self, path: str):
        """A convenience decorator for adding PUT routes to default router."""
        return self.default_router.put(path)

    def post(self, path: str):
        """A convenience decorator for adding POST routes to default router."""
        return self.default_router.post(path)

    def delete(self, path: str):
        """A convenience decorator for adding DELETE routes to default router."""
        return self.default_router.delete(path)
