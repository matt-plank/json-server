from typing import Callable

from ..request import Request
from ..response import Response

Middleware = Callable[[Request], Response]
MiddlewareDefinition = Callable[[Request, Middleware], Response]
