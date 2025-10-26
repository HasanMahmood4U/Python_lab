import pandas as pd
import numpy as np

# 1. Create a sample DataFrame with missing values
print("--- Original DataFrame ---")
data = {
    'Feature_A': [10, 20, np.nan, 40, 50, 60],
    'Feature_B': [1.5, np.nan, 2.5, 3.5, np.nan, 5.5],
    'Feature_C': ['A', 'B', 'C', np.nan, 'E', 'F']
}
df = pd.DataFrame(data)
print(df)
print("\nNumber of missing values per column:")
print(df.isnull().sum())

# --- Strategy 1: Impute Missing Values in 'Feature_A' with the MEAN ---

# 2. Calculate the mean of 'Feature_A'
mean_a = df['Feature_A'].mean()
print(f"\nCalculated Mean for Feature_A: {mean_a:.2f}")

# 3. Fill missing values in 'Feature_A'
# We use .copy() to ensure we are working on a new DataFrame to prevent warnings
df_mean_imputed = df.copy()
df_mean_imputed['Feature_A'].fillna(mean_a, inplace=True)

# --- Strategy 2: Impute Missing Values in 'Feature_B' with the MEDIAN ---

# 4. Calculate the median of 'Feature_B'
median_b = df['Feature_B'].median()
print(f"Calculated Median for Feature_B: {median_b:.2f}")

# 5. Fill missing values in 'Feature_B'
df_median_imputed = df_mean_imputed.copy()
df_median_imputed['Feature_B'].fillna(median_b, inplace=True)

# 6. Display the final imputed DataFrame
print("\n--- Final Imputed DataFrame ---")
print(df_median_imputed)

print("\nNumber of missing values per column in final DataFrame:")
print(df_median_imputed.isnull().sum())
# Note: Feature_C (categorical) still has one missing value, as we only imputed
# numerical columns.
