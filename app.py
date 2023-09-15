import pandas as pd
import matplotlib.pyplot as plt

# import CSV file as DataFrame using Pandas
ds = pd.read_csv('assets/real_estate.csv', sep=';')


# EXERCISE 01

# copy row that has the highest price to new variable
most_expensive_house = ds.loc[ds["price"].idxmax()]

# extract the address and price from previous variable
address = most_expensive_house["address"]
price = most_expensive_house["price"]

# print a sentence about the most expensive house 
print("The house with address " + address + " is the most expensive and its price is " + str(price) + " USD")

print(" ") # line break


# EXERCISE 02
### The CSV, oddly enough, contains houses with prices of 0.
### Not sure if this exercise would want me to ignore that, but I've gone ahead and done so.
# copy over all rows that have prices higher than 0
cheapest_house = ds[ds['price'] > 0]
# narrow down to lowest nonzero price
cheapest_house = cheapest_house.loc[cheapest_house["price"].idxmin()]

# extract the address and price from previous variable
address = cheapest_house["address"]
price = cheapest_house["price"]

# print a sentence about the cheapest house 
print("The house with address " + address + " is the cheapest and its price is " + str(price) + " USD")

print(" ") # line break


# EXERCISE 03

# copy rows for biggest and lowest surfaces to new variables
biggest_house = ds.loc[ds["surface"].idxmax()]
smallest_house = ds.loc[ds["surface"].idxmin()]

# extract the address and surface size from previous variables
address_biggest = biggest_house["address"]
address_smallest = smallest_house["address"]
surface_biggest = biggest_house["surface"]
surface_smallest = smallest_house["surface"]

# print a sentence about the largest house
print("The bigger house is located on " + address_biggest + " and its surface is " + str(int(surface_biggest)) + " meters")
# print a sentence about the smallest house
print("The smaller house is located on " + address_smallest + " and its surface is " + str(int(surface_smallest)) + " meters")

print(" ") # line break


# EXERCISE 04
# pull all houses' populations and drop duplicates
populations = ds["level5"].drop_duplicates()
# create an array list of populations
populations = populations.tolist()

print(populations)

print(" ") # line break


# EXERCISE 05
# check if any value in each column is null
column_nulls = ds.isnull().any()
# check for null values in rows
row_nulls = ds.isnull().any(axis=1)

# check if any value at all is null
any_nulls = column_nulls.any()

print(any_nulls)

print("Columns containing null values:")
print(ds.columns[column_nulls].to_list())

print(" ") # line break


# EXERCISE 06
row_count = ds.shape[0]
column_count = ds.shape[1]
print("Before deletions, there were " + str(row_count) + " rows and " + str(column_count) + " columns")

# ds.dropna(axis=0, inplace=True) # // rows
ds.dropna(axis=1, inplace=True) # // columns

print(" ")
row_count = ds.shape[0]
column_count = ds.shape[1]
print("After deletions, there are " + str(row_count) + " rows and " + str(column_count) + " columns")

print(" ") # line break


# EXERCISE 07
madrid_rows = ds[ds["level5"] == "Arroyomolinos (Madrid)"]

mean_prices = madrid_rows["price"].mean()

print("The mean price of all homes in Madrid is " + str(mean_prices))

print(" ") # line break


# EXCERCISE 08
prices = ds['price']

# Create a histogram
plt.hist(prices, bins=30)
plt.xlabel('prices')
plt.title('Prices of homes in Madrid')
# plt.grid(True)

# Show the histogram
plt.show()