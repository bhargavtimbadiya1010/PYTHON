'''47.Write a program to handle missing data using
drop na and fill na methods. '''

import pandas as pd

data = {
    "Name": ["Asha", "Rahul", "Neha", "Amit"],
    "Age": [20, None, 19, 22],
    "Marks": [85, 90, None, 88]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df.to_string(index=False))

print("\nAfter dropna():")
print(df.dropna().to_string(index=False))

print("\nAfter fillna():")
print(df.fillna(0).to_string(index=False))

