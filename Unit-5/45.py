'''45.Write a program to perform basic data analysis
using Pandas Data Frame. '''

import pandas as pd

data = {
    "Name": ["Asha", "Rahul", "Neha", "Amit"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df.to_string(index=False))

print("\nAverage Marks:", df["Marks"].mean())

print("Highest Marks:", df["Marks"].max())

print("\nStudents scoring 85 or more:")
print(df[df["Marks"] >= 85].to_string(index=False))
