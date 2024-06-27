def convert_decimal_to_roman(num):
    if num == 0:
        return 'Roman numerals have no zero'
    elif num < 0:
        return 'Roman numerals do not include negative numbers'
    elif num == 1:
        return 'I'
    elif num == 2:
        return 'II'
