import unittest
import calc

#Check https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug




class TestCalc(unittest.TestCase):
    # Must start with test_
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        #note the order and the argument
        ## self.assertRaises(ValueError, calc.divide, 10, 0)
        # hence a more preferred way of doing it is the following
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


# if you don't have a main here you have to run with python -m unittest test_calc.py
if __name__ == "__main__":
    unittest.main()