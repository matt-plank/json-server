def test_get(client):
    response = client.get("/")

    assert response.status == 200
    assert response.body == "Hello, world!"


def test_get_bad_path(client):
    response = client.get("/bad-path")

    assert response.status == 404


def test_get_router_item(client):
    response = client.get("/item/")

    assert response.status == 200
    assert response.body == "This is an item"


def test_get_router_item_bad_path(client):
    """/item and /item/ should be different paths."""
    response = client.get("/item")

    assert response.status == 404
