import json
import logging
import socket

from .middleware import compose
from .middleware.json_headers import json_headers
from .middleware.server_error import server_error
from .middleware.stringify_json import stringify_json
from .middleware.types import Middleware, MiddlewareDefinition
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

        self.middlewares: list[MiddlewareDefinition] = []
        self.api_response: Middleware = self.router_response

        self.add_middleware(json_headers)
        self.add_middleware(stringify_json)
        self.add_middleware(server_error)

    def run(self, host: str, port: int):
        """Start listening for connections."""
        self.server_socket.bind((host, port))

        logging.info(f"Running on {host}:{port}")

        self.server_socket.listen(1)

        while self.running:
            client_socket, address = self.server_socket.accept()

            request: bytes = client_socket.recv(1024)
            response: bytes = self.bytes_response(request)

            client_socket.sendall(response)
            client_socket.close()

    def bytes_response(self, bytes: bytes) -> bytes:
        """Outermost abstraction of request handling, raw bytes in, raw bytes out."""
        request = from_string(bytes.decode("utf-8"))
        response = self.api_response(request)

        logging.info(f"{request.method} {request.path} - {response.status}")

        return f"HTTP/1.1 {response.status}\n\n{response.body}".encode("utf-8")

    def router_response(self, request: Request) -> Response:
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

    def add_middleware(self, middleware: MiddlewareDefinition) -> None:
        """Add a middleware to the API."""
        self.middlewares.append(middleware)
        self.api_response = self.compose_middleware()

    def wrap_middleware(self, middleware: MiddlewareDefinition) -> None:
        """Wrap all exising middlewares with a new middleware."""
        self.middlewares = [middleware] + self.middlewares
        self.api_response = self.compose_middleware()

    def compose_middleware(self) -> Middleware:
        """Run through tracked middlewares and compose them into a single function."""
        response_function: Middleware = self.router_response

        for middleware in reversed(self.middlewares):
            response_function = compose.from_definition(middleware, response_function)

        return response_function

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
