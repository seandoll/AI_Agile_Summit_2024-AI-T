import unittest

from decimal_to_roman import convert_decimal_to_roman


class TestRomanNumerals(unittest.TestCase):
    def test_convert_decimal_to_roman_zero(self):
        result = convert_decimal_to_roman(0)
        self.assertEqual(result, 'Roman numerals have no zero',
                         f"Expected 'Roman numerals have no zero', but got {result}")

    def test_convert_decimal_to_roman_negative(self):
        result = convert_decimal_to_roman(-1)
        self.assertEqual(result, 'Roman numerals do not include negative numbers',
                         f"Expected 'Roman numerals do not include negative numbers', but got {result}")

    def test_convert_decimal_to_roman_one(self):
        result = convert_decimal_to_roman(1)
        self.assertEqual(result, 'I', f"Expected 'I', but got {result}")

    def test_convert_decimal_to_roman_two(self):
        result = convert_decimal_to_roman(2)
        self.assertEqual(result, 'II', f"Expected 'II', but got {result}")

    def test_convert_decimal_to_roman_three(self):
        result = convert_decimal_to_roman(3)
        self.assertEqual(result, 'III', f"Expected 'III', but got {result}")

    def test_convert_decimal_to_roman_four(self):
        result = convert_decimal_to_roman(4)
        self.assertEqual(result, 'IV', f"Expected 'IV', but got {result}")


if __name__ == '__main__':
    unittest.main()
