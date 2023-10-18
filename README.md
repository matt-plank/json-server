[![Python Tests](https://github.com/matt-plank/json-server/actions/workflows/python-tests.yaml/badge.svg)](https://github.com/matt-plank/json-server/actions/workflows/python-tests.yaml)

# json-server

A simple, JSON-only web server implementation in Python.

## Setting Up

Clone and enter the repository

```bash
$ git clone https://github.com/matt-plank/json-server.git
$ cd json-server
```

Install requirements (in a virtual environment of your choice)

```bash
$ pip install -r requirements.txt
```

Install the package

```bash
$ pip install .  # for use
$ pip install -e .  # for development
```

## Usage

We can create a simple API like this:

```python
from json_server.api import Api
from json_server.request import Request
from json_server.response import Response

api = Api()


@api.get("/")
def index(request: Request) -> Response:
    return Response(
        status=200,
        headers={},
        json={"message": "Hello, world!"},
    )


if __name__ == "__main__":
    api.run("0.0.0.0", 8000)
```

And test our API with curl:

```bash
$ curl localhost:8000
# {"message": "Hello, world!"}
```

## Testing

```bash
$ python -m pytest
```
