from app import create_app

def test_healthcheck():
    client = create_app().test_client()
    resp = client.get("/healthcheck")
    assert resp.status_code == 200
    assert resp.json == {"status": "healthy"}

