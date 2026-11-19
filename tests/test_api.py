import unittest
from fastapi.testclient import TestClient
from app.main import app


class APITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_valid_event(self):
        event = {
            "device_id": "sim-01",
            "timestamp": "2026-11-19T12:00:00Z",
            "severity": "INFO",
            "message": "synthetic startup",
        }
        response = self.client.post("/validate", json=event)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["valid"])

    def test_invalid_event(self):
        response = self.client.post("/validate", json={"device_id": ""})
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
