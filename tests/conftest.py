from pytest import fixture

from simple_web.api import Api
from simple_web.request import Request
from simple_web.response import Response
from simple_web.testing import TestClient


@fixture
def api():
    api = Api()

    @api.default_router.get("/")
    def index(request: Request) -> Response:
        return Response(
            status=200,
            headers={},
            body="Hello, world!",
        )

    return api


@fixture
def client(api):
    return TestClient(api)
