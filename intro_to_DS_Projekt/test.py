import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\Surface Laptop 3\OneDrive\Documents\DataScience\intro_to_DS_Projekt\data.csv")

print(df.head()) # First 5 rows
print(df.tail()) # Last 5 rows
print(df.info()) # Summary of the DataFrame
print(df.describe()) # Statistical summary of numerical columns

print(df["customer_id"][1])# Access a specific column and row (2 operations here)
print(df.iloc[1, 0]) # Access a specific cell by row and column index
#col = 0  row = 1
#iloc is father because it is only one operation
# using loc
print(df.loc[0]) # Access a specific row by index label
print(df.loc[1]) # Access a specific row by index label
