from typing import Callable

from .methods import Method
from .request import Request
from .response import Response

Route = tuple[str, Method]
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
            self.routes[(path, Method.GET)] = handler
            return handler

        return decorator

    def response_404(self, request: Request) -> Response:
        """A 404 response handler."""
        return Response(
            status=404,
            headers={},
            body="Not found",
        )

    def __contains__(self, route: Route) -> bool:
        """Checks whether a route is in the router."""
        return route in self.routes
