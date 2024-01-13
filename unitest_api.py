import requests
import unittest
import argparse
import sys

class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_url = API_URL

    def test_get_request(self):
        """ Test GET request to a sample API endpoint """
        response = requests.get(f'{self.api_url}')
        self.assertEqual(response.status_code, 200)
        #self.assertIn('userId', response.json())

    #def test_post_request(self):
    #    """ Test POST request to a sample API endpoint """
    #    data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    #    response = requests.post(f'{self.api_url}/posts', json=data)
    #    self.assertEqual(response.status_code, 201)
    #    self.assertEqual(response.json()['title'], data['title'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="API Test")
    parser.add_argument('api_url', type=str, help='URL of the API to test')
    args, unknown = parser.parse_known_args()
    API_URL = args.api_url

    # Run unittest with only the arguments it understands
    unittest.main(argv=[sys.argv[0]] + unknown)
