import unittest
from unittest.mock import MagicMock
from mylambda import lambda_handler, add_user, get_user_by_user_id, get_user_by_user_name, delete_user_by_user_id

class TestLambdaFunction(unittest.TestCase):
    def setUp(self):
        # Setup any necessary configurations or test data
        self.mock_s3_client = MagicMock()
        self.mock_s3_client.get_object.return_value = {
            'Body': MagicMock(read=MagicMock(return_value='[{"id": 1, "name": "user1"}]'))
        }

    def test_lambda_handler_check_id(self):
        event = {'queryStringParameters': {'operation': 'check_id', 'user_id': '1'}}
        context = {}
        response = lambda_handler(event, context, s3=self.mock_s3_client)
        expected_response = {
            'statusCode': 200,
            'body': '{"receivedParam1": "check_id", "receivedParam2": "1", "full_name": null, "Data": [{"id": 1, "name": "user1"}], "message": {"id": 1, "name": "user1"}}',
            'headers': {'Content-Type': 'application/json'}
        }
        self.assertEqual(response, expected_response)

    def test_add_user(self):
        data = [{"id": 1, "name": "user1"}]
        user_name = "user2"
        result = add_user(data, user_name)
        self.assertTrue(result)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[-1]['name'], user_name)

    def test_get_user_by_user_id_found(self):
        data = [{"id": 1, "name": "user1"}]
        user_id = "1"
        user = get_user_by_user_id(data, user_id)
        self.assertEqual(user, {"id": 1, "name": "user1"})

    def test_get_user_by_user_id_not_found(self):
        data = [{"id": 1, "name": "user1"}]
        user_id = "2"
        user = get_user_by_user_id(data, user_id)
        self.assertIsNone(user)

    # Add similar tests for get_user_by_user_name, delete_user_by_user_id, and other functions

if __name__ == '__main__':
    unittest.main()