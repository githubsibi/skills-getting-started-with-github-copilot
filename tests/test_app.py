from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_student_can_be_unregistered():
    original_participants = list(activities["Chess Club"]["participants"])

    try:
        response = client.delete(
            "/activities/Chess Club/unregister?email=michael@mergington.edu"
        )

        assert response.status_code == 200
        assert response.json()["message"] == (
            "Removed michael@mergington.edu from Chess Club"
        )
        assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
    finally:
        activities["Chess Club"]["participants"] = original_participants
