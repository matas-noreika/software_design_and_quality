import unittest

#importing employee class from employee module
from EmployeeClass import Employee

#create test case that inherits from 'unittest.TestCase'
class TestEmployee(unittest.TestCase):

    #1st test
    def test_email(self):
        print('test_email')
        
        #create employee information
        emp_1 = Employee('Corey','Schafer',50000)
        emp_2 = Employee('Sue','Smith',60000)
        
        #test employee email
        self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@email.com')
        
        #insert name change and retest
        emp_1.first = 'John'
        emp_2.first = 'Lucy'
        
        #retest to check naming is correct
        self.assertEqual(emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Lucy.Smith@email.com')


    def test_fullname(self):
        print('test_fullname')
        
        #create employee information
        emp_1 = Employee('Corey','Schafer',50000)
        emp_2 = Employee('Sue','Smith',60000)
        
        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Sue Smith')

        #insert name change and retest
        emp_1.first = 'John'
        emp_2.first = 'Lucy'

        self.assertEqual(emp_1.fullname, 'John Schafer')
        self.assertEqual(emp_2.fullname, 'Lucy Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        
        emp_1 = Employee('Corey','Schafer',50000)
        emp_2 = Employee('Sue','Smith',60000)
        
        emp_1.apply_raise()
        emp_2.apply_raise()

        #insert pay raise check and retest
        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)

if __name__ == '__main__':
    unittest.main()

