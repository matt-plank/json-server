from pytest import fixture

from simple_web.api import Api
from simple_web.request import Request
from simple_web.response import Response
from simple_web.router import Router
from simple_web.testing import TestClient


@fixture
def api():
    api = Api()

    router = Router()

    @router.get("/")
    def item(request: Request) -> Response:
        return Response(
            status=200,
            headers={},
            body="This is an item",
        )

    @api.get("/")
    def index(request: Request) -> Response:
        return Response(
            status=200,
            headers={},
            body="Hello, world!",
        )

    api.add_router("/item", router)

    return api


@fixture
def client(api):
    return TestClient(api)
