# Program: Check whether a number is Even or Odd
# ------------------------------------------------
# This program asks the user to enter an integer number, then determines if the
# number is even or odd and displays the result.
#
# Key idea:
# - An integer is Even if it is divisible by 2 (i.e., remainder 0 when divided by 2)
# - An integer is Odd if it is not divisible by 2 (i.e., remainder 1 when divided by 2)
# We use the modulo operator (%) to get the remainder of a division.

# 1) Read input from the user as text, then convert it to an integer using int(...)
num = int(input("Enter a number: "))

# 2) Use modulo (num % 2) to check divisibility by 2
#    - If remainder is 0, the number is Even
#    - Otherwise, it is Odd
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Notes:
# - If you input a non-integer (like letters), int(...) will raise a ValueError.
#   To make this more robust, you could wrap the conversion in a try/except.
# - Another fast method is to use bitwise AND: (num & 1) == 0 means Even.

