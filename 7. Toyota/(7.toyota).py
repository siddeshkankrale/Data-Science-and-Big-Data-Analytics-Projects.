#7. Perform the following operations using Python on the given data sets 
#(Toyota.csv)
#a. Remove all missing values
#b. display datatypes and concise summary of all numeric variables
#c. Remove All duplicate records 
#d. Apply Z-score Normalization on Price Column
#e. shape and reshape using pivot_ table


import pandas as pd
import numpy as np

data=pd.read_csv('C:/Users/Niraj/OneDrive/Documents/Dsbda/Dsbda/B1/Toyota.csv')

print("First few rows of the dataset:")
print(data.head())

data = data.dropna()

print("\nDatatypes and concise summary of all numeric variables:")
print(data.select_dtypes(include=['int64', 'float64']).info())


data = data.drop_duplicates()

mean_price = data['Price'].mean()
std_price = data['Price'].std()
data['Price_ZScore'] = (data['Price'] - mean_price) / std_price

print("\nShape of the dataset before reshaping:", data.shape)

pivot_table = data.pivot_table(index='CC', columns='FuelType', values='Price', aggfunc='mean')

print("\nShape of the dataset after reshaping using pivot_table:", pivot_table.shape)

print("\nPivot table:")
print(pivot_table)