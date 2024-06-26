#   2. Perform the following operations using Python on the given data sets (Toyota.csv)
#   a. Data cleaning
#   b. Data integration
#   c. Data transformation
#   d. Error correcting

import pandas as pd 
import numpy as np

# treat nan missing values as nan
cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=['??','????'])
cars_data1=cars_data.copy(deep=True)
# Observe shape and values of dataset
cars_data1.shape
cars_data1.info()
cars_data1.head(10)
cars_data1.head
cars_data1.describe()

##-------------------------------DATA CLEANING-----------------------------------------------

des = cars_data.describe()
#check count of missing values present in each column 
cars_data.isnull().sum()
# replacing nan values for numeric variables by mean / median of that variable
cars_data['Age'].fillna(cars_data['Age'].mean())
cars_data['Age'].fillna(cars_data['Age'].mean(),inplace=True)
cars_data['HP'].fillna(cars_data['HP'].mean(),inplace=True)
cars_data['KM'].fillna(cars_data['KM'].median(),inplace=True)
null_sum = cars_data.isnull().sum()

# remove duplicate records 
cars_data.drop_duplicates()

# replacing nan values for categorcal variables 
cars_data['FuelType'].value_counts()
#- get mode of such variables for count series
cars_data['FuelType'].value_counts().index[0]
cars_data['FuelType'].fillna(cars_data['FuelType'].value_counts().index[0],inplace=True)
cars_data['MetColor'].fillna(cars_data['MetColor'].value_counts().index[0],inplace=True)
# check that all column data is corrected
cars_data.isnull().sum()


##-------------------------------DATA INTEGRATION-----------------------------------------------
d1={'roll no':[1,2,3,4,5,6,7,8,9,10],'StudentName':['raj','sunil','raam','mahesh','jon','deepk','pooja','gaurav','nikita','fazal'],'age':[22,23,22,22,23,22,22,22,23,23]}
df1=pd.DataFrame(d1)
d2={'roll no':[1,3,8,9,10,11,12,13,14,15],'StudentName':['raj','raam','gautam','suraj','yogesh','anil','gitesh','sudip','sameer','malik'],'age':[22,22,22,23,22,22,23,22,22,22]}
df2=pd.DataFrame(d2)

merged=pd.merge(df1,df2)  # integate common records- inner join
merged_df=pd.merge(df1,df2, on='roll no')# merging records for common Roll nos in both Datasets 


##-------------------------------DATA TRANSFORMATION-----------------------------------------------
cars_data.dtypes
# Converting datatype explicitly
cars_data['MetColor']=cars_data['MetColor'].astype('object')
cars_data['Automatic']=cars_data['Automatic'].astype('object')
cars_data.dtypes
cars_data['Price']=cars_data['Price'].astype('float')
cars_data['KM']=cars_data['KM'].astype('int')
cars_data['KM']=cars_data['KM'].astype('int64')

# Decimal Scaling Normalization [Defining a transformation function]
cars_data['Price'].max() # 5 digit value
## Price is in scale of ten thousands so normalize we can devide data by 100000 to get LL Vlues in 0 to 1
def DScale_normalize(x):
    return x / 100000

cars_data['Price'] =DScale_normalize(cars_data['Price'])
cars_data['KM'] =DScale_normalize(cars_data['KM'])

##-------------------------------DATA ERROR CORRECTION-----------------------------------------------

## Replce to set uniform format
print(np.unique(cars_data['Doors'])) # array(['2', '3', '4', '5', 'five', 'four', 'three']

cars_data['Doors'].replace('three',3,inplace=True)
cars_data['Doors'].replace('four',4,inplace=True)
cars_data['Doors'].replace('five',5,inplace=True)