def test_index(client):
    response = client.get('/')
    assert response.json() == dict(message='Hello Template')
