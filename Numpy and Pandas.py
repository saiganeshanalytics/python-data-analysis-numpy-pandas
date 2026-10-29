#Numpy Array Operations

# Create a 1D NumPy Array

import numpy as np
import pandas as pd

temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

print(temperatures_w1)

# Inspect Array Properties

print(temperatures_w1.shape)
print(temperatures_w1.dtype)
print(temperatures_w1.size)

# Array Operations

# Convert Celsius to Fahrenheit
fahrenheit = (temperatures_w1 * 9/5) + 32

print("Temperatures in Fahrenheit:")
print(fahrenheit)

# Find the maximum temperature
print("Maximum Temperature:", np.max(temperatures_w1))

# Find the minimum temperature
print("Minimum Temperature:", np.min(temperatures_w1))

# Find the mean temperature
print("Mean Temperature:", np.mean(temperatures_w1))

# Array Slicing and Indexing

# Extract temperatures for the first three days
print("First Three Days:", temperatures_w1[0:3])

# Extract weekend temperatures (last two days)
print("Weekend Temperatures:", temperatures_w1[-2:])

# Extract the middle three days
print("Middle Three Days:", temperatures_w1[2:5])

# Create a 2D NumPy Array

temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]
])

print("Temperatures for Both Weeks:")
print(temperatures)

# Inspect and Slice the 2D Array

# Display the shape
print("Shape:", temperatures.shape)

# Display the data type
print("Data Type:", temperatures.dtype)

# Display the total number of elements
print("Total Elements:", temperatures.size)

# Extract temperatures for Week 1
print("Week 1 Temperatures:", temperatures[0])

# Extract temperatures for Week 2
print("Week 2 Temperatures:", temperatures[1])

# Extract weekend temperatures for Week 1
print("Week 1 Weekend Temperatures:", temperatures[0, -2:])

# Extract weekend temperatures for Week 2
print("Week 2 Weekend Temperatures:", temperatures[1, -2:])


# Pandas Series

# Create a Pandas Series

marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=["Rank1", "Rank2", "Rank3", "Rank4", "Rank5"]
)

print(marks)


# Indexing and Slicing:

# Access the 1st rank student's mark
print("Mark of 1st rank student:", marks.iloc[0])

# Retrieve the top 3 ranks using loc
print("\nTop 3 Ranks:")
print(marks.loc[["Rank1", "Rank2", "Rank3"]])

# Retrieve the mark of the 3rd rank student using iloc
print("\nMark of 3rd Rank Student:")
print(marks.iloc[2])

# Find ranks with marks greater than 90
print("\nRanks with Marks Greater Than 90:")
print(marks[marks > 90])

# Manipulating Series:

# Modify the 1st rank student's mark to 100
marks.loc["Rank1"] = 100

print("\nMarks After Updating Rank1:")
print(marks)

# Remove the Rank5 entry
marks = marks.drop("Rank5")

print("\nMarks after removing Rank5:")
print(marks)

# Calculate CGPA by dividing each mark by 10
cgpa = marks / 10

print("\nCGPA of each rank:")
print(cgpa)

# Pandas DataFrame:

# Create a transactions DataFrame
transactions = {
    "TransactionID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "ProductCategory": [
        "Electronics", "Clothing", "Electronics", "Furniture", "Clothing",
        "Electronics", "Furniture", "Clothing", "Furniture", "Electronics"
    ],
    "Region": [
        "North", "South", "North", "East", "West",
        "North", "East", "West", "South", "North"
    ],
    "Amount": [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
}

transactions = pd.DataFrame(transactions)

print("\nTransactions DataFrame:")
print(transactions)

# Data Exploration:

# Display the first 5 rows
print("\nFirst 5 Transactions:")
print(transactions.head())

# Display the last 5 rows
print("\nLast 5 Transactions:")
print(transactions.tail())

# Display the number of rows and columns
print("\nDataFrame Shape:")
print(transactions.shape)

# Display column names
print("\nColumn Names:")
print(transactions.columns)

# Display data types
print("\nData Types:")
print(transactions.dtypes)

# Display ProductCategory and Amount columns
print("\nProduct Category and Amount:")
print(transactions[["ProductCategory", "Amount"]])

# Retrieve the last 3 columns using iloc
print("\nLast 3 Columns Using iloc:")
print(transactions.iloc[:, -3:])

# Filter transactions where Region is North and Amount is greater than 200
print("\nNorth Region Transactions with Amount Greater Than 200:")

filtered_transactions = transactions[
    (transactions["Region"] == "North") &
    (transactions["Amount"] > 200)
]

print(filtered_transactions)

# Count transactions in each product category
print("\nProduct Category Value Counts:")
print(transactions["ProductCategory"].value_counts())

# Find unique regions
print("\nUnique Regions:")
print(transactions["Region"].unique())

# Calculate the mean amount for each region
print("\nAverage Transaction Amount by Region:")
print(transactions.groupby("Region")["Amount"].mean())

# Manipulating the DataFrame:

# Update the Amount for TransactionID 102 to 165
transactions.loc[transactions["TransactionID"] == 102, "Amount"] = 165

print("\nDataFrame After Updating Transaction 102:")
print(transactions)

# Add a Discount column equal to 10% of Amount
transactions["Discount"] = transactions["Amount"] * 0.10

print("\nDataFrame After Adding Discount:")
print(transactions)

# Remove the row with TransactionID 109
transactions = transactions[
    transactions["TransactionID"] != 109
]

print("\nDataFrame After Removing Transaction 109:")
print(transactions)

# Delete the Discount column
transactions = transactions.drop(columns=["Discount"])

print("\nFinal Transactions DataFrame:")
print(transactions)