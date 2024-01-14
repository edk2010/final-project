import requests
import unittest
import sys

class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_url = API_URL

    def test_get_request(self):
        """Test GET request to a sample API endpoint"""
        response = requests.get(self.api_url)
        self.assertEqual(response.status_code, 200)
        # Additional assertions can be added here

if __name__ == "__main__":
    if len(sys.argv) > 1:
        API_URL = sys.argv.pop(1)  # Pop the URL argument and assign it
    else:
        raise ValueError("No URL provided as a command-line argument")

    unittest.main()
