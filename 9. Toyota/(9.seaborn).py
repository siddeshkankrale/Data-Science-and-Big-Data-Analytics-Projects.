#9. Visualize the data  Python seaborn library by plotting histogram, scatter-plotand bar-plot
#a. Age vs Price- Scatter plot
#b. Distribution of KM data - Histogram with/without default kernel density
#estimate
#c. Bar plot




import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


cars_data = pd.read_csv('/home/niraj/Desktop/dsbda/B1/Toyota.csv')

# Scatter plot - Age vs Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Price', data=cars_data)
plt.title('Scatter plot of Age vs Price')
plt.xlabel('Age')
plt.ylabel('Price')
plt.show()

# Histogram of KM data with kernel density estimate
plt.figure(figsize=(10, 6))
sns.histplot(cars_data['KM'], kde=True)
plt.title('Histogram of KM data with KDE')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.show()

# Histogram of KM data without kernel density estimate
plt.figure(figsize=(10, 6))
sns.histplot(cars_data['KM'], kde=False)
plt.title('Histogram of KM data without KDE')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.show()

# Bar plot of FuelType
plt.figure(figsize=(8, 5))
sns.countplot(x='FuelType', data=cars_data, palette='Set2')
plt.title('Bar plot of FuelType')
plt.xlabel('FuelType')
plt.ylabel('Count')
plt.show()
