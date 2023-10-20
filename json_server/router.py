from typing import Callable

from .request import Request
from .response import Response

Route = tuple[str, str]
RequestHandler = Callable[[Request], Response]


class Router:
    """Responsible for connecting requests to the correct handlers."""

    def __init__(self):
        """Initialise router with space for routes."""
        self.routes: dict[Route, RequestHandler] = {}

    def find(self, route: Route) -> RequestHandler:
        """Find a route by path and method."""
        if route not in self.routes:
            return self.response_404

        return self.routes[route]

    def get(self, path: str):
        """Decorator to add a GET route."""

        def decorator(handler: RequestHandler):
            self.routes[(path, "GET")] = handler
            return handler

        return decorator

    def put(self, path: str):
        """Decorator to add a PUT route."""

        def decorator(handler: RequestHandler):
            self.routes[(path, "PUT")] = handler
            return handler

        return decorator

    def post(self, path: str):
        """Decorator to add a POST route."""

        def decorator(handler: RequestHandler):
            self.routes[(path, "POST")] = handler
            return handler

        return decorator

    def delete(self, path: str):
        """Decorator to add a DELETE route."""

        def decorator(handler: RequestHandler):
            self.routes[(path, "DELETE")] = handler
            return handler

        return decorator

    def response_404(self, request: Request) -> Response:
        """A 404 response handler."""
        return Response(
            status=404,
            headers={},
            json={"message": "Not found"},
        )

    def __contains__(self, route: Route) -> bool:
        """Checks whether a route is in the router."""
        return route in self.routes
