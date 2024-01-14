import requests
import unittest
import os
import sys

class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_url = os.environ.get('API_URL')
        cls.api_url = sys.argv[1]
        
    def test_get_request(self):
        """Test GET request to a sample API endpoint"""
        response = requests.get(f'{self.api_url}')
        self.assertEqual(response.status_code, 200)
        # Additional assertions can be added here

# Below code ensures argparse is used only when running directly
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="API Test")
    parser.add_argument('api_url', type=str, help='URL of the API to test')
    args = parser.parse_args()
    API_URL = sys.argv[1]
    #os.environ['API_URL'] = args.api_url
    unittest.main()
