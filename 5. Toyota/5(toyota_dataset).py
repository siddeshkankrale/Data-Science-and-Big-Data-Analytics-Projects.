'''
5. Perform the following operations using Python on the given data sets (Toyota.csv)
    a. Remove missing values
    b. set Doors Value to uniform format
    c. Provide concise summary of all numeric variables
    d. Remove All duplicate records
    e. Get dummies for categorical data Fuel type
'''

import pandas as pd 
import numpy as np

# treat nan missing values as nan
cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=['??','????'])
cars_data1=cars_data.copy(deep=True)
# Observe shape and values of dataset
cars_data1.shape
# -------------------------------[A]Remove missing values---------------------------------

#check count of missing values present in each column 
cars_data.isnull().sum()
# replacing nan values for numeric variables by mean / median of that variable
cars_data['Age'].fillna(cars_data['Age'].mean(),inplace=True)
cars_data['HP'].fillna(cars_data['HP'].mean(),inplace=True)
cars_data['KM'].fillna(cars_data['KM'].median(),inplace=True)
null_sum = cars_data.isnull().sum()


# replacing nan values for categorcal variables 
cars_data['FuelType'].value_counts()
cars_data['FuelType'].fillna(cars_data['FuelType'].value_counts().index[0],inplace=True)
cars_data['MetColor'].fillna(cars_data['MetColor'].value_counts().index[0],inplace=True)
cars_data.isnull().sum()

# -------------------------------[B]Set Doors Value to uniform format---------------------------------

## Replce to set uniform format
print(np.unique(cars_data['Doors'])) # array(['2', '3', '4', '5', 'five', 'four', 'three']
cars_data['Doors'].replace('three',3,inplace=True)
cars_data['Doors'].replace('four',4,inplace=True)
cars_data['Doors'].replace('five',5,inplace=True)

# -------------------------------[C]Provide concise summary of all numeric variables---------------------------------
des = cars_data.describe()
cars_data1.info()


# -------------------------------[D]Remove All duplicate records---------------------------------
cars_data.drop_duplicates()


# -------------------------------[E]Get dummies for categorical data Fuel type---------------------------------
cars_sub1=cars_data[['Price','Age','FuelType','Automatic']]
dummy_df1=pd.get_dummies(cars_sub1,columns=['FuelType'])
dummy_df2=pd.get_dummies(cars_sub1,columns=['FuelType','Automatic'])


