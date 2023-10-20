import logging

from ..request import Request
from ..response import Response
from .types import Middleware


def server_error(request: Request, inner_middleware: Middleware) -> Response:
    """Catch any exceptions raised by the inner middleware and return a response from the server."""
    try:
        response = inner_middleware(request)
    except Exception as e:
        logging.exception(e)

        response = Response(
            status=500,
            json={"message": "Internal server error"},
        )

    return response
