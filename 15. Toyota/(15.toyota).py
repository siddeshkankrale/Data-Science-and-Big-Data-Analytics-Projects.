#5. Perform following operations on the given data set (Toyota.csv)
#1. Display shape and summary and count of missing values in the dataset
#2. Remove duplicate records
#3. Clean the data set- Replace the missing values in each column with appropriate
#value
#4. Convert the datatype of Metcolor and Automatic column in as object type




import pandas as pd

# Load the dataset
cars_data = pd.read_csv('/home/niraj/Desktop/dsbda/B1/Toyota.csv',index_col=0,na_values=['??','????'])
# 1. Display shape and summary and count of missing values in the dataset
print("Shape of the dataset:", cars_data.shape)
print("\nSummary of the dataset:")
print(cars_data.info())
print("\nCount of missing values in each column:")


# 2. Remove duplicate records
duplicates=cars_data.drop_duplicates(inplace=True)
print(duplicates)

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

check_dataype=cars_data.info()
print(check_dataype)
# 4. Convert the datatype of 'Metcolor' and 'Automatic' columns to object type


cars_data['Weight'] = cars_data['Weight'].astype('float64')
cars_data['Price'] = cars_data['Price'].astype('float64')

# Display the cleaned dataset
print("\nCleaned dataset:")
print(cars_data.head())
