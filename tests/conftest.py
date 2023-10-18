from json_server.api import Api
from json_server.request import Request
from json_server.response import Response
from json_server.router import Router
from json_server.testing import TestClient
from pytest import fixture


@fixture
def api():
    api = Api()

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

    @api.get("/")
    def index(request: Request) -> Response:
        return Response(
            status=200,
            json={"message": "Hello, world!"},
        )

    api.add_router("/item", router)

    return api


@fixture
def client(api):
    return TestClient(api)
