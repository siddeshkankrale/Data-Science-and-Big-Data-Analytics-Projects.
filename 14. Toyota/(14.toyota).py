#14. Perform following operations on the given data set (Toyota.csv)
#1. Get unique values of categorical ‘Doors’
#2. Transform of all values in same format
#3. Apply Decimal scaling normalization on HP column






import pandas as pd

cars_data = pd.read_csv('/home/niraj/Desktop/dsbda/B1/Toyota.csv',index_col=0,na_values=['??','????'])


cars_data.isnull().sum()


cars_data['Age'].fillna(cars_data['Age'].mean(),inplace=True)
cars_data['HP'].fillna(cars_data['HP'].mean(),inplace=True)
cars_data['KM'].fillna(cars_data['KM'].median(),inplace=True)
null_sum = cars_data.isnull().sum()

cars_data['FuelType'].fillna(cars_data['FuelType'].value_counts().index[0],inplace=True)
cars_data['MetColor'].fillna(cars_data['MetColor'].value_counts().index[0],inplace=True)
null_sum = cars_data.isnull().sum()


cars_data['Doors'].replace('three',3,inplace=True)
cars_data['Doors'].replace('four',4,inplace=True)
cars_data['Doors'].replace('five',5,inplace=True)

unique_doors = cars_data['Doors'].unique()
print("Unique values of 'Doors':", unique_doors)

# 2. Transform all values in the same format
# Assuming you want to transform all 'Doors' values to lowercase
cars_data['Doors'] = cars_data['Doors'].str.lower()

# 3. Apply Decimal scaling normalization on HP column
max_hp = cars_data['HP'].max()
cars_data['HP_normalized'] = cars_data['HP'] / (10 ** len(str(max_hp)))

# Display the transformed data
print("\nTransformed dataset with normalized HP:")
print(cars_data[['Doors', 'HP', 'HP_normalized']].head())
