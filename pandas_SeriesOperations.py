import pandas as pd

# Creating a Pandas Series
data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("Series:\n", data)

# -------------------------
# Indexing Operations
# -------------------------
print("\nIndexing by label:", data['b'])      # Access element with label 'b'
print("Indexing by position:", data[2])      # Access element at index position 2

# Multiple index labels
print("\nMultiple labels:\n", data[['a', 'c', 'e']])

# -------------------------
# Slicing Operations
# -------------------------
print("\nSlicing by label:\n", data['b':'d'])   # Includes both start and end labels
print("\nSlicing by position:\n", data[1:4])     # End index is excluded

# -------------------------
# Querying Operations
# -------------------------
print("\nQuery: values greater than 30:\n", data[data > 30])
print("\nQuery: even numbers:\n", data[data % 2 == 0])
