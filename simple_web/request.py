from dataclasses import dataclass


@dataclass
class Request:
    """Represents a request to the API."""

    method: str
    path: str
    headers: dict[str, str]


def from_string(request_string: str) -> Request:
    """Parse a request from a string."""
    request_lines = request_string.split("\r\n")

    method, path, _ = request_lines[0].split(" ")

    headers: dict[str, str] = {}
    for header_line in request_lines[1:]:
        if header_line == "":
            break

        try:
            key, value = header_line.split(": ")
            headers[key] = value
        except ValueError:
            raise ValueError(f"Invalid header line: {header_line!r}")

    return Request(
        method=method,
        path=path,
        headers=headers,
    )
