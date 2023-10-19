from dataclasses import dataclass, field


@dataclass
class Response:
    """Represents a response from the API."""

    status: int
    json: dict
    headers: dict[str, str] = field(default_factory=dict)
