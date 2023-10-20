from pytest import fixture

from json_server.api import Api
from json_server.request import Request
from json_server.response import Response
from json_server.router import Router
from json_server.testing import TestClient


@fixture
def item_router():
    router = Router()

    @router.get("/")
    def item(request: Request) -> Response:
        return Response(
            status=200,
            json={"message": "This is an item"},
        )

    @router.post("/")
    def create_item(request: Request) -> Response:
        return Response(
            status=201,
            json={"message": "Created an item"},
        )

    return router


@fixture
def exception_router():
    router = Router()

    @router.get("/")
    def raise_exception(request: Request) -> Response:
        raise Exception("This is an exception")

    return router


@fixture
def api(item_router, exception_router):
    api = Api()
    api.add_router("/item", item_router)
    api.add_router("/exception", exception_router)

    @api.get("/")
    def index(request: Request) -> Response:
        return Response(
            status=200,
            json={"message": "Hello, world!"},
        )

    return api


@fixture
def client(api):
    return TestClient(api)
