import unittest
from string_calc import StringCalculator


class StringCalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_double(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_new_line(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            self.calculator.add("1,\n")

    def test_custom(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_negative(self):
        with self.assertRaises(ValueError) as cm:
            self.calculator.add("1,-2,-3")
        self.assertEqual(str(cm.exception), "negatives not allowed: -2,-3")

    def test_ignore(self):
        self.assertEqual(self.calculator.add("2,1001"), 2)

    def test_custom_unknown(self):
        self.assertEqual(self.calculator.add("//[***]\n1***2***3"), 6)

    def test_multiple(self):
        self.assertEqual(self.calculator.add("//[*][%]\n1*2%3"), 6)

    def test_multiple_unknown(self):
        self.assertEqual(self.calculator.add("//[**][%%%]\n1**2%%%3"), 6)


if __name__ == '__main__':
    unittest.main()
