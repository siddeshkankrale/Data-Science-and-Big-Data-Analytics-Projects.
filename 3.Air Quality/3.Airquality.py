#   3. Perform the following operations using Python on the airquality dataset
#   a. Read data set and display summary
#   b. Create data subsets based on observations and constraints
#   c. Merge observations of any two subsets
#   d. Transpose data in subset
#   e. Apply Sort Data on Temp values

import pandas as pd
import numpy as np

air_data = pd.read_csv("/Users/omgol/OneDrive/Desktop/Dsbda/final/3.Air Quality/airquality.csv")
air_data1 = air_data.copy(deep = True)
air_data.info()

#--------------create subsets based on observations and constraints--------------------------
df1 = air_data1[['Ozone','Solar.R','Wind','Temp']]
df2 = air_data1[['Ozone','Solar.R','Wind','Temp']].loc[0:30]
df3 = air_data1[(air_data1['Wind']>10)&(air_data1['Temp']>50)]

#-------------------Read data set and display summary-------------
df1.info()
df2.info()
df3.info()

#-------------------Merge observations of any two subsets---------------
merge1 = pd.concat([df1,df2])
merge2 = pd.concat([df2,df3])

#-------------------Transpose data in subset-----------------
tranpsose1 = df1.transpose()
tranpsose2 = df2.transpose()
tranpsose3 = df3.transpose()

#------------------Sort Data on Temp Values-----------------
sort1 = df1.sort_values('Temp')
sort2 = df2.sort_values('Temp',ascending = True)
sort3 = df3.sort_values('Temp',ascending = False) 