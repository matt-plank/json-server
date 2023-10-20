from ..request import Request
from ..response import Response
from .types import Middleware, MiddlewareDefinition


def from_definition(middleware: MiddlewareDefinition, next_function: Middleware) -> Middleware:
    """Compose a middleware function from a definition and a next function."""

    def middleware_function(request: Request) -> Response:
        return middleware(request, next_function)

    return middleware_function
