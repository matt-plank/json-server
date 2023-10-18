from pytest import fixture

from simple_web.api import Api
from simple_web.testing import TestClient


@fixture
def api():
    return Api()


@fixture
def client(api):
    return TestClient(api)
