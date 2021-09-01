import pandas as pd
import numpy as np


# read data
data = pd.read_csv('dataset/NFL Play by Play 2009-2017 (v4).csv')
print(data.head())

# calculate the number of missing value in each column
missing_value_count = data.isnull().sum()
print(missing_value_count)

# calculate how much data missing
total_values = np.product(data.shape)
total_missing = missing_value_count.sum()
print(f'{total_missing / total_values * 100:.3f} %')

# drop missing value
# data = data.dropna()
# data = data.dropna(axis=1)

# fill missing value
data = data.fillna(0)
# data = data.fillna(method='ffill')
print(data)
