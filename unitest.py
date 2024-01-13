import unittest
from mylambda import lambda_handler, add_user, get_user_by_user_id, get_user_by_user_name, delete_user_by_user_id




class TestUserFunctions(unittest.TestCase):
    def test_add_user(self):
        data = [{"id": 1, "name": "user1"}]
        user_name = "user2"
        result = add_user(data, user_name)
        self.assertTrue(result)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[-1]['name'], user_name)

    def test_get_user_by_user_id_found(self):
        data = [{"id": 1, "name": "user1"}]
        user_id = 1  
        user = get_user_by_user_id(data, user_id)
        self.assertEqual(user, {"id": 1, "name": "user1"})

    def test_get_user_by_user_id_not_found(self):
        data = [{"id": 1, "name": "user1"}]
        user_id = 2  
        user = get_user_by_user_id(data, user_id)
        self.assertIsNone(user)


if __name__ == '__main__':
    unittest.main()
