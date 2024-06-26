#10. Visualize the data using Python matplotlib library by plotting histogram, scatter-plot
#and bar-plot
#a. Age vs Price- Scatter plot
#b. Distribution of KM data - histogram
#c. FuelType wise CarsCount- Barplot



import matplotlib.pyplot as plt
import pandas as pd

cars_data = pd.read_csv('/home/niraj/Desktop/dsbda/B1/Toyota.csv')
# Scatter plot - Age vs Price
plt.figure(figsize=(10, 6))
plt.scatter(cars_data['Age'], cars_data['Price'])
plt.title('Scatter plot of Age vs Price')
plt.xlabel('Age')
plt.ylabel('Price')
plt.show()

# Histogram of KM data
plt.figure(figsize=(10, 6))
plt.hist(cars_data['KM'], bins=20, edgecolor='black')
plt.title('Histogram of KM data')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.show()

# Bar plot of FuelType wise CarsCount
plt.figure(figsize=(8, 5))
fuel_type_counts = cars_data['FuelType'].value_counts()
plt.bar(fuel_type_counts.index, fuel_type_counts.values, color=['blue', 'green', 'red'])
plt.title('Bar plot of FuelType wise CarsCount')
plt.xlabel('FuelType')
plt.ylabel('Count')
plt.show()
