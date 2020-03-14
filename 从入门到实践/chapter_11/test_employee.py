import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """测试Employee类"""
    
    def setUp(self):
        self.employee = Employee('Ac','Dx',20000)
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,25000)
    def test_give_custom_raise(self):
        self.employee.give_raise(2000)
        self.assertEqual(self.employee.salary,22000)

unittest.main()