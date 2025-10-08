import pandas as pd

df = pd.read_csv(r"C:\Users\Surface Laptop 3\OneDrive\Documents\DataScience\intro_to_DS_Projekt\data.csv")

print(df.head()) # First 5 rows
print(df.info()) # Summary of the DataFrame
print(df.describe()) # Statistical summary of numerical columns
