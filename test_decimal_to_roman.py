import unittest

from decimal_to_roman import convert_decimal_to_roman


class TestRomanNumerals(unittest.TestCase):
    def test_convert_decimal_to_roman_one(self):
        result = convert_decimal_to_roman(1)
        self.assertEqual(result, 'I', f"Expected 'I', but got {result}")


if __name__ == '__main__':
    unittest.main()
