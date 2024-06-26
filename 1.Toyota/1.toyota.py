#1. Perform the following operations using Python on the given datasets(Toyota.csv)
#a. Create data subsets
#b. Merge Data
#c. Sort Data on any specified column values
#. Transposing Data
#. Shape and reshape Data

import pandas as pd
import numpy as np

cars_data = pd.read_csv("/Users/omgol/OneDrive/Desktop/Dsbda/final/1.Toyota/Toyota.csv") 
cars_data1 = cars_data.copy(deep = True)

cars_data1.describe()
cars_data1.head
cars_data1.head(10)
cars_data1.info()

#--------creating subsets--------------------
df1 = cars_data1[['Price','Age','KM']]
df2 = cars_data1[['FuelType','HP','MetColor']]
df3 = cars_data1[(cars_data1['Price']>15000)&(cars_data1['Age']<8)]

df4 = cars_data1[['Price','Age','KM','FuelType']].loc[0:10]
df5 = cars_data1[['FuelType','HP','MetColor']].loc[10:30]

#--------merge data-----------------------------
merge1 = pd.concat([df1,df2,df3])
merge2 = pd.concat([df2,df3])
merge3 = pd.concat([df1,df4])
merge4 = pd.concat([df1,df2,df3,df4])

#----------sort data-------------------------------
sort1 = cars_data1.sort_values('Price')
sort2 = cars_data1.sort_values('Price', ascending = False)

#----------transpose data--------------------------
transposing = df5.transpose()

#----------shape and reshape data------------------
pivot_table = pd.pivot_table(df4,index=['Age','FuelType'],values='Price')