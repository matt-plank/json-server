def test_get(client):
    response = client.get("/")

    assert response.status == 200
