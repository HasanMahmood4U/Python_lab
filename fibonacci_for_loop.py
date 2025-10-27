# Program: Print first n Fibonacci numbers using a for loop
# Safe input handling & user-friendly messages

MAX_N = 1000  # optional safety limit to avoid extremely large output

# Read number of terms (n) from the user with validation
while True:
    raw = input("Enter how many Fibonacci numbers to print (n): ").strip()
    try:
        n = int(raw)
        if n < 0:
            print("Please enter a non-negative integer (0 or greater).")
            continue
        if n > MAX_N:
            print(f"Please enter a smaller number (<= {MAX_N}).")
            continue
        break
    except ValueError:
        print("Invalid input — please enter a valid integer (e.g. 10).")

# If n is 0, nothing to print (or you can print a message)
if n == 0:
    print("No numbers to show (n = 0).")
else:
    a, b = 0, 1
    print(f"First {n} Fibonacci number{'s' if n>1 else ''}:")
    for _ in range(n):
        print(a)
        a, b = b, a + b
