from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    starting_participants = list(activities[activity_name]["participants"])

    try:
        response = client.delete(f"/activities/{activity_name}/unregister?email={email}")

        assert response.status_code == 200
        payload = response.json()
        assert payload["message"] == f"Unregistered {email} from {activity_name}"
        assert email not in activities[activity_name]["participants"]
    finally:
        activities[activity_name]["participants"] = starting_participants
