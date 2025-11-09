import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv("data.csv")
#print(df.head(1)) 

# Check for missing values
missing_values = df.isnull().sum() # 0 missing values in each column
sns.heatmap(missing_values.to_frame(), annot=True, cmap='viridis')
plt.title('Missing Values Heatmap')
#plt.show()

duplicated_valus = df.duplicated().sum() # 0 duplicate rows

#Feature engineering example
""" avrage_salary = df["estimated_salary"].mean()
avrage_balance = df["balance"].mean()

df["IsHighValueCustomer"] = 0
df.loc[(df["estimated_salary"] > avrage_salary) & (df["balance"] > avrage_balance), "IsHighValueCustomer"] = 1
df["IsHighValueCustomer"].value_counts() #2996 high value customers

df["IsActiveWithBalance"] = 0
df.loc[(df["balance"] > 0) & (df["active_member"] == 1), "IsActiveWithBalance"] = 1
df["IsActiveWithBalance"].value_counts() # 3278 active customers with balance

df["IsActiveWithoutBalance"] = 0
df.loc[(df["balance"] == 0) & (df["active_member"] == 1), "IsActiveWithoutBalance"] = 1
df["IsActiveWithoutBalance"].value_counts() # 1873 active without balance customers

df["IsInactiveWithBalance"] = 0
df.loc[(df["balance"] > 0) & (df["active_member"] == 0), "IsInactiveWithBalance"] = 1
df["IsInactiveWithBalance"].value_counts() #3105 inactive with balance customers

df["IsInactiveWithoutBalance"] = 0
df.loc[(df["balance"] == 0) & (df["active_member"] == 0), "IsInactiveWithoutBalance"] = 1
df["IsInactiveWithoutBalance"].value_counts() # 1744 inactive without balance customers

min_age = df["age"].min() #18
max_age = df["age"].max() #92
bins = [min_age, 24, 45, 60, 75, max_age] 
labels = ["Young", "Adult", "Middle-Aged", "Senior", "elderly"]
df["AgeGroup"] = pd.cut(df["age"], bins=bins, labels=labels, include_lowest=True)
agegroup = df["AgeGroup"].value_counts() #Adult / 7432  Middle-Aged / 1647  Young / 457  Senior / 419  elderly / 45  
 """
df.to_csv("preproccessed_data.csv", index=False)

# Load the preprocessed data with new features
preproccess_df = pd.read_csv("preproccessed_data.csv")