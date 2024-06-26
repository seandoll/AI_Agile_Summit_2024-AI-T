import unittest

from decimal_to_roman import convert_decimal_to_roman


class TestRomanNumerals(unittest.TestCase):
    def test_convert_decimal_to_roman_zero(self):
        result = convert_decimal_to_roman(0)
        self.assertEqual(result, 'Roman numerals have no zero',
                         f"Expected 'Roman numerals have no zero', but got {result}")


if __name__ == '__main__':
    unittest.main()
