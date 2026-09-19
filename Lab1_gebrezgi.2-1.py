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

    total = (odd_sum * 3) + even_sum
    remainder = total % 10

    if remainder == 0:
        return 0
    return 10 - remainder

upc = input("Enter a 12-digit UPC: ")

first_11_digits = upc[0:11]
check_digit = upc[11]

print()
print("The first 11 digits are '" + first_11 + "'.")
print("The given check digit is '" + check_digit + "'.")

print()
print("Calculating digit")
check_digit = find_UPC(first_11_digits)
print("The check digit is " + str(check_digit) + ".")