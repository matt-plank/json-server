from .api import Api
from .request import Request
from .response import Response


class TestClient:
    """Client for testing user-defined APIs."""

    def __init__(self, api: Api):
        """Initialise the test client with an API to run against."""
        self.api = api

    def get(self, path: str, headers: dict[str, str] = {}) -> Response:
        """Run a GET request against the API."""
        request = Request(
            method="GET",
            path=path,
            headers=headers,
        )

        response = self.api.api_response(request)

        return response

    def put(self, path: str, headers: dict[str, str] = {}) -> Response:
        """Run a PUT request against the API."""
        request = Request(
            method="PUT",
            path=path,
            headers=headers,
        )

        response = self.api.api_response(request)

        return response

    def post(self, path: str, headers: dict[str, str] = {}) -> Response:
        """Run a POST request against the API."""
        request = Request(
            method="POST",
            path=path,
            headers=headers,
        )

        response = self.api.api_response(request)

        return response

    def delete(self, path: str, headers: dict[str, str] = {}) -> Response:
        """Run a DELETE request against the API."""
        request = Request(
            method="DELETE",
            path=path,
            headers=headers,
        )

        response = self.api.api_response(request)

        return response
