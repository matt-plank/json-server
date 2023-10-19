import json

from ..request import Request
from ..response import Response
from .types import Middleware


def stringify_json(request: Request, next_middleware: Middleware) -> Response:
    """Set the Content-Type header to application/json."""
    response = next_middleware(request)
    response.body = json.dumps(response.json)

    return response
