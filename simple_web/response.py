from dataclasses import dataclass


@dataclass
class Response:
    """Represents a response from the API."""

    status: int
    headers: dict[str, str]
    body: str
