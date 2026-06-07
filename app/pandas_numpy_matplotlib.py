""""
Ok we had lots of fun playing around with hardcoded data

But let's use a "real" .csv dataset and use all 3 technologies we've learned

We'll start by finally using a Pandas dataframe to load and manipulate the real data
Then use Numpy to do some calculations to use in our chart
And visualize the data with Matplotlib!
"""""
from math import trunc

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load in the CSV data into a Pandas DataFrame
df = pd.read_csv("data/sales_data.csv")
print(df.head())
print(df.describe())
print(df.info())
print(df.shape)
print(df.columns)
print(df.dtypes)

"""
PANDAS DATA CLEANING

We need to "clean up" the data
-One record has N/A for the product name
-A few records have a negative number for units sold
"""
df = df[df["product"].notna()]
print(df.to_string())

# Replacing values in the dataframe to turn negative units sold into 0
# TODO: Is setting 0 the best way to handle this? Depends on why the values are negative...
# df = df[df["units_sold"] >= 0]
# print(df.to_string())

"""""
    OR THIS 
"""""
# df = df.query("units_sold > 0")
# print(df.to_string())
"""""
OR do this
"""""

# Replacing values in the dataframe to turn negative units sold into 0
# TODO: Is setting 0 the best way to handle this? Depends on why the values are negative...
df["units_sold"] = df["units_sold"].clip(lower=0) # values will be 0 AT LOWEST
print(df.to_string())
"""
PANDAS DATA TRANSFORMATION

The data is "clean" now, but we'd like to reformat it to help with our analysis
Right now each row is one product/region/month combo
But we want total units sold per product per month!!

groupby() groups rows together! We'll see it below
"""

monthly_product_sales = df.groupby(["month", "product"])["units_sold"].sum().reset_index()
print(monthly_product_sales.to_string())
print(type(monthly_product_sales)) # it's a dataframe because of the reset_index() added at the end otherwise it would be panda-series return

# Isolate each type of product into DataFrames (more visibility, easier plotting)
laptops = monthly_product_sales[monthly_product_sales["product"] == "Laptop"].reset_index()
print(laptops.to_string())

headphones = monthly_product_sales[monthly_product_sales["product"] == "Headphones"].reset_index()
print(headphones.to_string())

keyboards = monthly_product_sales[monthly_product_sales["product"] == "Keyboard"].reset_index()
print(keyboards.to_string())

print("===== Monthly Product Sales =====")
print(monthly_product_sales)

print("~~~~~ Laptop Sales ~~~~~")
# Print without the product name column
print(laptops[["month", "units_sold"]])

print("~~~~~ Headphones Sales ~~~~~")
# Let's get the same result, but by excluding columns instead of naming the ones we want
print(headphones[["month", "units_sold"]])

print("~~~~~ Keyboard Sales ~~~~~")
# use loc to filter out columns we don't want and include columns we do
print(keyboards[["month", "units_sold"]])


"""
NUMPY CALCULATIONS

Convert the data into Numpy Arrays, and calculate the overall average
We'll use this average in our chart!
"""

all_units = monthly_product_sales["units_sold"].values
print(all_units)

overall_average = np.mean(all_units)
print(f"Average Sales Overall: {overall_average:.2f}")
best_sales = np.max(all_units)
print(f"Best sales Overall: {best_sales}")
worst_sales = np.min(all_units)
print(f"Worst sales Overall: {worst_sales}")

# LET's PLOT --------________-----------__________--------_______------

#Using the Dataframe we defined above
plt.plot(laptops["month"], laptops["units_sold"], marker="o", label="Laptop", linewidth=2)
plt.plot(headphones["month"], headphones["units_sold"], marker="s", label="Headphones", linewidth=2)
plt.plot(keyboards["month"], keyboards["units_sold"], marker="^", label="Keyboard", linewidth=2)
plt.title("Monthly Product Sales")
plt.xlabel("Months")
plt.ylabel("Units sold")
plt.legend()
plt.grid(True, alpha=0.5)
# plt.show()

print("===================(Creating, Updating, Deleting Files)")

# Remember, we READ from a file at the very top of this script

# Using our initial "df" dataframe - tell Pandas to NOT make a new index
df.to_csv("data/sales_data_cleaned.csv", index=False)

# add a new column in the DataFrame with name overall_avg
df["overall_avg_sales"] = overall_average
# Our numpy calculation above
print(df.to_string())
# Save this enriched file (overwrite the one we already saved)
df.to_csv("data/sales_data_cleaned.csv", index=False)

# We CAN change files directly without overwriting
with open("data/sales_data_cleaned.csv", "a") as file:
    file.write(df.to_string())

# Create and delete a new file (cuz I don't want to delete my old files)
df.to_json("data/sales.json", index=False)

import os
if os.path.isfile("data/sales.json"):
    os.remove("data/sales.json")
# if os.path.isfile("data/sales_data_cleaned.csv"):
#     os.remove("data/sales_data_cleaned.csv")






