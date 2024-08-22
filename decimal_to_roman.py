def convert_decimal_to_roman(num):
    if num == 0:
        return 'Roman numerals have no zero'
    elif num < 0:
        return 'Roman numerals do not include negative numbers'

    roman_numerals = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII'}
    return roman_numerals.get(num)