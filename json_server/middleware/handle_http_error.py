from ..exceptions import HTTPError
from ..request import Request
from ..response import Response
from .types import Middleware


def handle_http_error(request: Request, inner_middleware: Middleware) -> Response:
    """Catch any exceptions raised by the inner middleware and return a response from the server."""
    try:
        response = inner_middleware(request)
    except HTTPError as e:
        response = Response(
            status=e.status_code,
            json={"message": e.message},
        )

    return response
