'''46.Write a program to create a Data Frame from
CSV or Excel files.'''

import pandas as pd

data = pd.read_csv("ipl_dataset_dv.csv")

df = pd.DataFrame(data)

print("Data from CSV file:")
print(df.head(5))
