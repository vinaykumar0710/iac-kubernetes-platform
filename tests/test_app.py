import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from app import app


class ApplicationTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_returns_application_metadata(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["application"], "iac-platform-app")
        self.assertEqual(data["status"], "running")

    def test_health_endpoint(self):
        response = self.client.get("/healthz")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "healthy")

    def test_readiness_endpoint(self):
        response = self.client.get("/readyz")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ready")


if __name__ == "__main__":
    unittest.main()
