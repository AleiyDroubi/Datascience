import pandas as pd
import matplotlib.pyplot as plt
from pygments import highlight
import seaborn as sns

# Read the CSV file
df = pd.read_csv("data.csv")
#print(df.head(1)) 

# Check for missing values
missing_values = df.isnull().sum() # 0 missing values in each column
#sns.heatmap(missing_values.to_frame(), annot=True, cmap='viridis')
#plt.title('Missing Values Heatmap')
#plt.show()

duplicated_valus = df.duplicated().sum() # 0 duplicate rows

#Feature engineering example
avrage_salary = df["estimated_salary"].mean()
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

df.to_csv("preproccessed_data.csv", index=False)

# Load the preprocessed data with new features
preproccess_df = pd.read_csv("preproccessed_data.csv")

#scaling on all numerical features except customer_id...
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
numerical_features = [ "age", "balance", "estimated_salary"]
preproccess_df[numerical_features] = scaler.fit_transform(preproccess_df[numerical_features]) 
#credit score and tenure and product_numbr will scale later if needed


#categorial to numerical encoding
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
catagorical_features = ["gender"]
preproccess_df["gender"]= label_encoder.fit_transform(preproccess_df[catagorical_features])

preproccess_df["country_france"] = 0
preproccess_df.loc[preproccess_df["country"] == "France", "country_france"] = 1

preproccess_df["country_germany"] = 0
preproccess_df.loc[preproccess_df["country"] == "Germany", "country_germany"] = 1

preproccess_df["country_spain"] = 0
preproccess_df.loc[preproccess_df["country"] == "Spain", "country_spain"] = 1

preproccess_df=preproccess_df.drop("country", axis =1)

#one hot encoding for age group
agegroup_dummies = pd.get_dummies(preproccess_df["AgeGroup"], prefix="AgeGroup")
preproccess_df = pd.concat([preproccess_df, agegroup_dummies], axis=1)
preproccess_df = preproccess_df.drop("AgeGroup", axis=1)

preproccess_df = preproccess_df.drop("customer_id", axis=1) #dropping customer id as it is not needed for modeling

preproccess_df.to_csv("final_preproccessed_data.csv", index=False)

final_data = pd.read_csv("final_preproccessed_data.csv")

(final_data["AgeGroup_Young"].value_counts()) # 457
(final_data["AgeGroup_Middle-Aged"].value_counts()) # 1647
(final_data["AgeGroup_Senior"].value_counts()) # 419
(final_data["AgeGroup_elderly"].value_counts()) # 45
(final_data["AgeGroup_Adult"].value_counts()) # 7432

#print(final_data.info())

#No outliers in all data except score credite but e need them
