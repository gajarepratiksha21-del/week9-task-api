
from app import create_app


def test_register():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/auth/register",
        json={
            "username": "pytestuser",
            "email": "pytestuser@example.com",
            "password": "test12345"
        }
    )

    assert response.status_code in [201, 409]


def test_login():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/auth/login",
        json={
            "email": "test@example.com",
            "password": "test12345"
        }
    )

    assert response.status_code in [200, 401]
