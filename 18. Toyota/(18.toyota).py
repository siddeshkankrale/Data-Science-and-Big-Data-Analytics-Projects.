#18. Perform following operations on the given data set (Toyota.csv)
#1. Create Subset selecting columns 'Price', 'Age', 'FuelType', 'Automatic'
#2. Create subset having records of all Petrol vehicles
#3. Create subset of cars’ data having Price greater than 15000 and Age less than 8
#4. Merge records the above two data subsets





import pandas as pd

# Load the dataset
cars_data = pd.read_csv('/home/niraj/Desktop/dsbda/B1/Toyota.csv')

# 1. Create Subset selecting columns 'Price', 'Age', 'FuelType', 'Automatic'
subset1 = cars_data[['Price', 'Age', 'FuelType', 'Automatic']]

# 2. Create subset having records of all Petrol vehicles
petrol_subset = cars_data[cars_data['FuelType'] == 'Petrol']

# 3. Create subset of cars’ data having Price greater than 15000 and Age less than 8
subset2 = cars_data[(cars_data['Price'] > 15000) & (cars_data['Age'] < 8)]

# 4. Merge records of the above two data subsets
merged_subset = pd.concat([petrol_subset, subset2])

# Displaying results
print("Subset selecting columns 'Price', 'Age', 'FuelType', 'Automatic':")
print(subset1.head())

print("\nSubset of all Petrol vehicles:")
print(petrol_subset.head())

print("\nSubset of cars’ data with Price greater than 15000 and Age less than 8:")
print(subset2.head())

print("\nMerged records of the above two data subsets:")
print(merged_subset.head())
