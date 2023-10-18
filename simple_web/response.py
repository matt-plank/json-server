from dataclasses import dataclass, field


def default_headers():
    """Returns a default set of headers."""
    return {
        "Content-Type": "application/json",
    }


@dataclass
class Response:
    """Represents a response from the API."""

    status: int
    json: dict
    headers: dict[str, str] = field(default_factory=default_headers)
