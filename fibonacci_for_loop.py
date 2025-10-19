# Program: Print first n Fibonacci numbers using a for loop
# --------------------------------------------------------
# The Fibonacci sequence starts with 0 and 1. Each next number is the sum of the
# previous two numbers: 0, 1, 1, 2, 3, 5, 8, ...
# This script reads n from the user and prints the first n numbers of the sequence.

# Read number of terms (n) from the user and convert to integer
n = int(input("Enter how many Fibonacci numbers to print (n): "))

# Initialize the first two Fibonacci numbers
a = 0
b = 1

# Use a for loop to print n terms
for _ in range(n):
    print(a)
    # Update the pair: next term becomes a+b, shift forward
    a, b = b, a + b

