#17. Perform following operations on the given data set (Toyota.csv)
#1. Add a new column ‘Revised’ to the dataset specifying 5% increase in old Price.
#2. Create subset of cars’ data having Price greater than 15000 and Age less than 8
#3. Sort observations in descending order of Revised Price
#4. Apply ZScore_normalize on HP column



import pandas as pd

# Load the dataset
cars_data = pd.read_csv('/home/niraj/Desktop/dsbda/B1/Toyota.csv')


# 1. Add a new column ‘Revised’ to the dataset specifying 5% increase in old Price
cars_data['Revised'] = cars_data['Price'] * 1.05

# 2. Create a subset of cars’ data having Price greater than 15000 and Age less than 8
subset = cars_data[(cars_data['Price'] > 15000) & (cars_data['Age'] < 8)]

# 3. Sort observations in descending order of Revised Price
cars_data.sort_values(by='Revised', ascending=False, inplace=True)

# 4. Apply ZScore_normalize on HP column
cars_data.info()


cars_data['HP']=cars_data['HP'].replace('????',110,inplace=True)
cars_data['HP'] = cars_data['HP'].astype('float64')
cars_data['HP'].fillna(cars_data['HP'].mode(),inplace=True)
mean_hp = cars_data['HP'].mean()
std_hp = cars_data['HP'].std()
cars_data['HP_ZScore'] = (cars_data['HP'] - mean_hp) / std_hp

# Displaying results
print("Dataset with a new 'Revised' column and subset of cars' data with Price greater than 15000 and Age less than 8:")
print(subset)

print("\nDataset sorted in descending order of 'Revised' Price:")
print(cars_data.head())

print("\nDataset with ZScore normalized 'HP' column:")
print(cars_data[['HP', 'HP_ZScore']].head())
