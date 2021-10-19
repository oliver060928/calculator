import unittest

def calculate(a, operator, b):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(3, "+", 3), 6)

    def test_subtraction(self):
        self.assertEqual(calculate(3, "-", 2), 1)

    def test_multiplication(self):
        self.assertEqual(calculate(3, "*", 3), 9)

    def test_division(self):
        self.assertEqual(calculate(3, "/", 1), 3)



if __name__ == "__main__":
    unittest.main()
