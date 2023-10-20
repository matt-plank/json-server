def test_get(client):
    response = client.get("/")

    assert response.status == 200
    assert response.json == {"message": "Hello, world!"}
    assert response.headers == {"Content-Type": "application/json"}


def test_get_bad_path(client):
    response = client.get("/bad-path")

    assert response.status == 404
    assert response.json == {"message": "Not found"}
    assert response.headers == {"Content-Type": "application/json"}


def test_get_router_item(client):
    response = client.get("/item/")

    assert response.status == 200
    assert response.json == {"message": "This is an item"}
    assert response.headers == {"Content-Type": "application/json"}


def test_get_router_item_bad_path(client):
    """/item and /item/ should be different paths."""
    response = client.get("/item")

    assert response.status == 404
    assert response.json == {"message": "Not found"}
    assert response.headers == {"Content-Type": "application/json"}


def test_put_on_get_route(client):
    response = client.put("/")

    assert response.status == 404
    assert response.json == {"message": "Not found"}
    assert response.headers == {"Content-Type": "application/json"}


def test_post(client):
    response = client.post("/item/")

    assert response.status == 201
    assert response.json == {"message": "Created an item"}
    assert response.headers == {"Content-Type": "application/json"}


def test_exception(client):
    response = client.get("/exception/")

    assert response.status == 500
    assert response.json == {"message": "Internal server error"}
    assert response.headers == {"Content-Type": "application/json"}
