import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(12, 2), 14)

    def test_add2(self):
        self.assertEqual(self.calc.add(5, 8), 13)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(10, 24), -14)

    def test_subtract3(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
    

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(12, -12), -144)
    
    def test_multiply3(self):
            self.assertEqual(self.calc.multiply(-12, -12), 144)

    def test_divide(self):
        self.assertEqual(self.calc.divide(12, -12), -1)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(12, 3), 4)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(50, 26),24)

    def test_modulo2(self):
            self.assertEqual(self.calc.modulo(100, 100),0)





    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()