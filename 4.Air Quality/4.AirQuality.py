#   4. Perform the following operations using Python on the airquality dataset
#   a. Create data subsets selecting specified columns and index range
#   b. Data cleaning to treat nan values
#   c. Data transformation- Apply Min-max Normalization on Wind Column
#   d. Plot Month wise Temperature using Matplotlib/ seaborn library

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

air_data = pd.read_csv('airquality.csv',na_values=['??','????'])
air_data1 = air_data.copy(deep = True)
air_data.info()

#------------------Data cleaning to treat NaN values---------------------------
air_data1.describe()
air_data1.isnull().sum()

# replacing nan values for numeric variables by mean / median of that variable
air_data1['Ozone'].fillna(air_data['Ozone'].mean())
air_data1['Ozone'].fillna(air_data['Ozone'].mean(),inplace = True)
air_data1['Solar.R'].fillna(air_data['Solar.R'].mean(),inplace = True)

# remove duplicate records 
air_data1.drop_duplicates()

#--------------create subsets based on observations and constraints--------------------------
df1 = air_data1[['Ozone','Solar.R','Wind','Temp']]
df2 = air_data1[['Ozone','Solar.R','Wind','Temp']].loc[0:30]
df3 = air_data1[(air_data1['Wind']>10)&(air_data1['Temp']>50)]

#--------Data transformation- Apply Min-max Normalization on Wind Column-------------------
def MinMax_normalize(x):
    return (x - x.min()) /(x.max()-x.min())

# Apply the transformation function to a column KM
MinMax_normalize(air_data1['Wind'])

air_data1['Wind'] =MinMax_normalize(air_data1['Wind'])

#----------plot--------------------

## [A] SCATTER PLOT
plt.scatter(air_data['Temp'],air_data['Month'],c='blue')
plt.title("Scatter Plot Temp vs Month")
plt.xlabel('Temp')
plt.ylabel('Month')
plt.show()

