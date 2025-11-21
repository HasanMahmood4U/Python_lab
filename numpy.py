
print("Array A:", A)
print("Array B:", B)

# Element-wise operations
print("\nElement-wise Addition:", A + B)
print("Element-wise Subtraction:", A - B)
print("Element-wise Multiplication:", A * B)
print("Element-wise Division:", A / B)

# Reshaping arrays
C = np.array([[1, 2], [3, 4], [5, 6]])  # 3x2 array
print("\nOriginal Array C:\n", C)

# Reshape to 2x3 array
D = C.reshape(2, 3)
print("\nReshaped Array D (2x3):\n", D)
# Reshape to 2x3 array