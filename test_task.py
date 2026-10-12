
from app import create_app


def test_tasks_require_login():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/tasks/")

    assert response.status_code == 401


def test_create_task_requires_login():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/tasks/",
        json={
            "title": "Learn Flask API",
            "description": "Practice task API"
        }
    )

    assert response.status_code == 401
