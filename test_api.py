
from app import create_app

app = create_app()
client = app.test_client()

login_response = client.post(
    "/api/auth/login",
    json={
        "email": "test@example.com",
        "password": "test12345"
    }
)

token = login_response.get_json()["access_token"]

headers = {
    "Authorization": f"Bearer {token}"
}

update_response = client.put(
    "/api/tasks/1",
    headers=headers,
    json={
        "title": "Learn Flask REST API Updated",
        "description": "Practice CRUD operations",
        "status": "in-progress",
        "priority": "high"
    }
)

print("Update Status:", update_response.status_code)
print("Update Response:", update_response.get_json())

delete_response = client.delete(
    "/api/tasks/1",
    headers=headers
)

print("Delete Status:", delete_response.status_code)
print("Delete Response:", delete_response.get_json())
