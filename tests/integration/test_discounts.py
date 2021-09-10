import unittest
import json

from app import create_app


class DiscountsAPITest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_calculate_net_amount(self):
        """Test the endpoint: /api/v1/bill/employee"""
        response = self.app.post(
            "/api/v1/bill/employee",
            data=json.dumps(
                {"amount": 990,
                 "years": 1,
                 "grocery_p": "False"}),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(
            response.get_json(),
            {"amount": 648})
