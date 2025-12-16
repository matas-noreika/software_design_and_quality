import unittest
import hello #import main file

class TestCalc(unittest.TestCase):

    def test_add(self): #all tests have to start with test_ for the program to recognise a test has been created
        result = hello.add(10, 5)
        self.assertEqual(result, 15) #prove that the answer should equal 15
        
    def test_subtract(self): #all tests have to start with test_ for the program to recognise a test has been created
        result = hello.subtract(10, 5)
        self.assertEqual(result, 4) #prove that the answer should equal 5  

    def test_multiply(self): #all tests have to start with test_ for the program to recognise a test has been created
        result = hello.multiply(10, 5)
        self.assertEqual(result, 50) #prove that the answer should equal 50        
        
    def test_divide(self): #all tests have to start with test_ for the program to recognise a test has been created
        result = hello.divide(10, 5)
        self.assertEqual(result, 2) #prove that the answer should equal 2
