import pandas as pd
import numpy as np

data = {
    "Age": [25, np.nan, 30, 22, np.nan],
    "Salary": [50000, 60000, np.nan, 52000, 58000],
    "City": ["Mumbai", "Delhi", None, "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)
print("\nMissing Values Count:\n", df.isnull().sum())

df = df.dropna(how="all")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])

# Forward fill
df = df.ffill()

df["Age"] = df["Age"].interpolate()
df["Salary"] = df["Salary"].interpolate()

print("\nCleaned DataFrame:\n", df)
print("\nRemaining Missing Values:\n", df.isnull().sum())