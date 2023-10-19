from ..request import Request
from ..response import Response
from .types import Middleware


def json_headers(request: Request, next_middleware: Middleware) -> Response:
    """Set the Content-Type header to application/json."""
    response = next_middleware(request)
    response.headers["Content-Type"] = "application/json"

    return response
