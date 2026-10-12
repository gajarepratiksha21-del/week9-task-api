
from app import create_app


def test_profile_without_token():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/users/me")

    assert response.status_code == 401
