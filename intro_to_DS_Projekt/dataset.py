import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")
#print(data.head(2))

#print(data.tail(2))

#print(data.info())

#print(data.describe())

#print(data.iloc[1, 0])  # Access a specific cell by row and column index

#print(data.loc[1, 'customer_id'])  # Access a specific cell by row label and column label

#print(data.loc[0])# Access a specific row by index label

female_customers_count = data["gender"].value_counts()["Female"]
print(female_customers_count)

female_id = data[data["gender"] == "Female"]["customer_id"]


plt.figure(figsize=(10, 6))
plt.hist(data[data["gender"]=="Female"] ['age'], bins=30, color='purple', alpha=0.7)
plt.title('Number of Female Customers')
plt.xlabel('Gender')
plt.ylabel('Count') 
plt.show()

femalebigger60 = data["gender"][data["age"] > 60].value_counts()["Female"]
print(femalebigger60)

#balance by geiography
plt.figure(figsize=(10, 6))
data.groupby('country')['balance'].mean().plot(kind='bar')
plt.title('Average Balance by Country')
plt.xlabel('Country')
plt.ylabel('Average Balance')
plt.show()