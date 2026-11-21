import unittest
from app import get_response

class TestNexoraBackend(unittest.TestCase):
    def test_application_name(self):
        self.assertEqual(
            get_response()["application"],
            "Nexora Cloud Platform"
        )

    def test_service_status(self):
        self.assertEqual(
            get_response()["status"],
            "running"
        )

if __name__ == "__main__":
    unittest.main()
