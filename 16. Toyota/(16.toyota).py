#16. Perform following operations on the given data set (Toyota.csv)
#1. Remove duplicate records from dataset and display concise summary
#2. Create Subset selecting columns 'Price', 'Age', 'FuelType' and initial 10 records.
#3. Transpose of this subset
#4. Apply mean-max normalization on HP column



import pandas as pd

# Load the dataset
cars_data = pd.read_csv('/home/niraj/Desktop/dsbda/B1/Toyota.csv')



# 1. Remove duplicate records from dataset and display concise summary
cars_data.drop_duplicates(inplace=True)
print("Summary after removing duplicates:")
print(cars_data.info())

# 2. Create Subset selecting columns 'Price', 'Age', 'FuelType' and initial 10 records
subset = cars_data[['Price', 'Age', 'FuelType']].head(10)

# 3. Transpose of this subset
transposed_subset = subset.transpose()

# 4. Apply mean-max normalization on HP column

# Convert 'HP' column to numeric
cars_data['HP'] = pd.to_numeric(cars_data['HP'])

# 4. Apply mean-max normalization on HP column
min_hp = cars_data['HP'].min()
max_hp = cars_data['HP'].max()
cars_data['HP_normalized'] = (cars_data['HP'] - min_hp) / (max_hp - min_hp)
print("\nDataset with mean-max normalized HP column:")
print(cars_data[['HP', 'HP_normalized']].head())


# Display the transposed subset and normalized dataset
print("\nTransposed subset:")
print(transposed_subset)
print("\nDataset after mean-max normalization on HP column:")
print(cars_data[['HP', 'HP_normalized']].head())
