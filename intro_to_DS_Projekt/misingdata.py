import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\Surface Laptop 3\OneDrive\Documents\DataScience\data.csv")
missing = (data.isnull().sum())  # Check for missing values in each column
#data.dropna(inplace=True)                # remove rows with missing data
# OR
#data.fillna(0, inplace=True)             # replace NaN with 0
print(data.describe())

 
#histograam
plt.figure(figsize=(10, 6))
plt.hist(data["age"],  color='blue', alpha=0.7)
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show() 


 
plt.hist(data["gender"], color='orange', alpha=0.7)
plt.title("Gender distribution")
plt.xlabel("Gender")
plt.ylabel("Frequency") 
plt.show()

#churn customers 
plt.figure(figsize=(10, 6))
churned_counts = data["churn"].value_counts()
plt.hist(data["churn"], color='green', alpha=0.7)
plt.title("Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Frequency")
plt.show()


#scatter
plt.figure(figsize=(12, 8))
plt.scatter(data["credit_score"], data["balance"], color='purple', alpha=0.6)
plt.title("Credit Score vs Balance")
plt.xlabel("Credit Score")
plt.ylabel("Balance")
plt.show()

#balance vs age
plt.figure(figsize=(12, 8))
plt.scatter(data['age'], data['balance'], color='orange', alpha=0.6)
plt.title('Balance vs Age')
plt.xlabel('Age')
plt.ylabel('Balance')   
plt.show()

#balance by geiography
plt.figure(figsize=(10, 6))
data.groupby('country')['balance'].mean().plot(kind='bar')
plt.title('Average Balance by Country')
plt.xlabel('Country')
plt.ylabel('Average Balance')
plt.show()