import pandas as pd

data = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Sales': [100, 150, 200, 130, 170, 220]
})

data.set_index('Product', inplace=True)

# Accessing data using the index
print(data.loc['A'])  # Access sales data for product A
print(data.loc['B'])  # Access sales data for product B
print(data.loc["C"])  # Access sales data for product C

df = pd.DataFrame({
    "product": ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"],
    "sales": [120, 150, 90, 200, 300, 80, 170]
})
df = df.sort_index()
print(df)  # Display the DataFrame sorted by index
sorted_df = df.sort_values(by="sales", ascending=False)
print(sorted_df)  # Display the DataFrame sorted by sales in descending order top 2
print(sorted_df.iloc[0])  # Access the first row of the sorted DataFrame
print(sorted_df.iloc[1])  # Access the second row of the sorted DataFrame
print(sorted_df.iloc[2])  # Access the last row of the sorted DataFrame
# Accessing data using iloc
print(df.iloc[0])  # Access the first row
print(df.iloc[1])  # Access the second row
print(df.loc[2])  # Access the third row

#hashtags
tags = ["#python", "#data", "#pandas", "#indexing", "#dataframe", "#python", "#pandas", "#python"]
count = {}
for tag in tags:
    count[tag] = count.get(tag, 0) + 1
print(count)
trend = max(count, key=count.get)
print(f"The most trending hashtag is {trend} with {count[trend]} occurrences.")

#max algon
numbers = [10, 25, 5, 40, 15]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    print(f"The maximum number is {max_num}")