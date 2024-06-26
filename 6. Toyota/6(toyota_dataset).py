"""
6. Perform the following operations using Python on the given data sets
(Toyota.csv)
a. Sort observations on Price values order
b. Create Subset by Selecting columns, selecting rows and columns,
c. Create subset of cars data having Price greater than 15000 and Age
less than 8
d. Create subset of cars data consuming Petrol
e. Apply decimal normalization on Price column

"""
import pandas as pd


df = pd.read_csv('Toyota.csv')

# a. Sort observations on Price values order

sorted_df = df.sort_values(by='Price')
print("sorted dataframe/n",sorted_df)

# b. Create Subset by Selecting columns, selecting rows and columns,

subset1 = df[['Price', 'Age', 'FuelType']]                  #Selecting columns

subset2 = df.loc[10:20, ['Price', 'Age', 'FuelType']]       #selecting rows and columns

print("Subset 1\n",subset1)
print("Subset 2\n",subset2)


#c. Create subset of cars data having Price greater than 15000 and Age less than 8

subset3 = df[(df['Price'] > 15000) & (df['Age'] < 8)]

print("Subset 3\n",subset3)

# d. Create subset of cars data consuming Petrol

subset4=df[df['FuelType']=='Petrol']
print("Subset 4\n",subset4)

# e. Apply decimal normalization on Price column

df['Price'].max() # 5 digit value
def DScale_normalize(x):
    return x / 100000

df['Price'] =DScale_normalize(df['Price'])