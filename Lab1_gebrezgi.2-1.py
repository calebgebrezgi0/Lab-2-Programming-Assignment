"""
UPC Validator
Caleb Gebrezgi
Validate 12-Digit UPC-A Code
September 19, 2026
"""

def find_UPC(first_11_digits):
    odd_sum = 0
    even_sum = 0

    for index in range(len(first_11_digits)):
        digit = int(first_11_digits[index])
        if index % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit