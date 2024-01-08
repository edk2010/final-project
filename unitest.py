import json
import unittest
from employees import app, get_employee, employee_is_valid, employees

class TestEmployeeFunctions(unittest.TestCase):

    def setUp(self):
        app.testing = True

    def test_get_employee(self):
        # Assuming there's an employee with id 1
        employee = get_employee(1)
        self.assertIsNotNone(employee)
        self.assertEqual(employee['id'], 1)
        self.assertEqual(employee['name'], 'Ashley')

        # Assuming there's no employee with id 100
        non_existent_employee = get_employee(100)
        self.assertIsNone(non_existent_employee)

    def test_employee_is_valid(self):
        valid_employee = {'name': 'John Doe'}
        self.assertTrue(employee_is_valid(valid_employee))

        invalid_employee = {'name': 'Jane Doe', 'position': 'Manager'}
        self.assertFalse(employee_is_valid(invalid_employee))

    def test_create_employee(self):
        initial_employee_count = len(employees)

        new_employee = {'name': 'John Doe'}
        app.test_client().post('/employees', data=json.dumps(new_employee), content_type='application/json')

        self.assertEqual(len(employees), initial_employee_count + 1)
        self.assertEqual(employees[-1]['name'], 'John Doe')

    def test_update_employee(self):
        # Assuming there's an employee with id 1
        updated_employee_data = {'name': 'Updated Name'}
        app.test_client().put('/employees/1', data=json.dumps(updated_employee_data), content_type='application/json')

        updated_employee = get_employee(1)
        self.assertIsNotNone(updated_employee)
        self.assertEqual(updated_employee['name'], 'Updated Name')

    def test_delete_employee(self):
        initial_employee_count = len(employees)

        # Assuming there's an employee with id 1
        app.test_client().delete('/employees/1')

        self.assertEqual(len(employees), initial_employee_count - 1)
        self.assertIsNone(get_employee(1))

if __name__ == '__main__':
    unittest.main()