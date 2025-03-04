def int_to_roman(num):
    """
    Convert an integer to a Roman numeral using only if-else statements.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    
    roman_number = ""

    # Handle 1000s
    if num >= 1000:
        roman_number += "M" * (num // 1000)
        num %= 1000

    # Handle 900
    if num >= 900:
        roman_number += "CM"
        num -= 900
    # Handle 500s
    elif num >= 500:
        roman_number += "D"
        num -= 500
    # Handle 400
    elif num >= 400:
        roman_number += "CD"
        num -= 400

    # Handle 100s
    if num >= 100:
        roman_number += "C" * (num // 100)
        num %= 100

    # Handle 90
    if num >= 90:
        roman_number += "XC"
        num -= 90
    # Handle 50s
    elif num >= 50:
        roman_number += "L"
        num -= 50
    # Handle 40
    elif num >= 40:
        roman_number += "XL"
        num -= 40

    # Handle 10s
    if num >= 10:
        roman_number += "X" * (num // 10)
        num %= 10

    # Handle 9
    if num == 9:
        roman_number += "IX"
        num -= 9
    # Handle 5s
    elif num >= 5:
        roman_number += "V"
        num -= 5
    # Handle 4
    elif num == 4:
        roman_number += "IV"
        num -= 4

    # Handle 1s
    if num >= 1:
        roman_number += "I" * num

    return roman_number

# Example usage
print(int_to_roman(1987))  # Output: MCMLXXXVII


