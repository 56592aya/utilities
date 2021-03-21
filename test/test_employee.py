import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):
#Note the prints for understanding
    @classmethod
    def setUpClass(cls):
        # If you have to run something before all tests or do something once before
        # note the camelCase

        print('setUpClass')
    
    @classmethod
    def tearDownClass(cls):
        # If you have to run something afterall tests or do something once after
        # note the camelCase
        print('tearDownClass')
    def setUp(self):
        #setUp is run before every single test
        # note the camelCase
        self.emp_1 = Employee('Arash', 'Yazdiha', 50000)
        self.emp_2 = Employee('Ashi', 'Mashi', 60000)
        print('setUp')
    def tearDown(self):
        # tearDown is run after every single test
        # note the camelCase
        print('tearDown')
        pass

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email,'Arash.Yazdiha@email.com')
        self.assertEqual(self.emp_2.email, 'Ashi.Mashi@email.com')

        self.emp_1.first = 'Mehrdad'
        self.emp_2.first = 'Mehrdad'

        self.assertEqual(self.emp_1.email, 'Mehrdad.Yazdiha@email.com')
        self.assertEqual(self.emp_2.email, 'Mehrdad.Mashi@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Arash Yazdiha')
        self.assertEqual(self.emp_2.fullname, 'Ashi Mashi')

        self.emp_1.first = 'Mehrdad'
        self.emp_2.first = 'Mehrdad'

        self.assertEqual(self.emp_1.fullname, 'Mehrdad Yazdiha')
        self.assertEqual(self.emp_2.fullname, 'Mehrdad Mashi')
    
    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
    
    def test_monthly_schedule(self):
        # we want to mock the requests.get in the employee module
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Yazdiha/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
           
            
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Mashi/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == "__main__":
    unittest.main()