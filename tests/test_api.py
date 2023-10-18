def test_get(client):
    response = client.get("/")

    assert response.status == 200
    assert response.body == "Hello, world!"


def test_get_bad_path(client):
    response = client.get("/bad-path")

    assert response.status == 404
