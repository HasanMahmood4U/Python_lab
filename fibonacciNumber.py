# Program to print first n Fibonacci numbers using a for loop

# Take input from the user
n = int(input("Enter the number of terms: "))

# Initialize first two terms
a, b = 0, 1

print("Fibonacci Series:")

# Use for loop to generate Fibonacci numbers
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
