#8. Visualize the data using Python libraries matplotlib / seaborn
#1. Scatter plot- Car-Price by Age
#2. Histogram on Cars data KM
#3. Bar plot on counts of FuelType category (Petrol, Disel and CNG)













import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



cars_data = pd.read_csv('/home/niraj/Desktop/dsbda/B1/Toyota.csv')


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Price', data=cars_data)
plt.title('Car Price by Age')
plt.xlabel('Age')
plt.ylabel(' Price')
plt.show()

# Histogram on Cars data KM
plt.figure(figsize=(10, 6))
sns.histplot(cars_data['KM'], bins=20, kde=True)
plt.title('Histogram of KM')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.show()

# Bar plot on counts of FuelType category (Petrol, Diesel, and CNG)
plt.figure(figsize=(8, 5))
sns.countplot(x='FuelType', data=cars_data, palette='Set2')
plt.title('Counts of FuelType Categories')
plt.xlabel('FuelType')
plt.ylabel('Count')
plt.show()
