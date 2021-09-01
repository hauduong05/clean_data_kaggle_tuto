import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read data
data = pd.read_csv('dataset/catalog.csv')

# parse data
data['date_parsed'] = pd.to_datetime(data['date'], format='%m/%d/%y')
print(data['date_parsed'].head())

# get day, month, year
print(data['date_parsed'].dt.day.head())
print(data['date_parsed'].dt.month.head())
print(data['date_parsed'].dt.year.head())

# plot
data_day = data['date_parsed'].dt.day
sns.displot(data_day, bins=31)
data_month = data['date_parsed'].dt.month
sns.displot(data_month, bins=12)
data_year = data['date_parsed'].dt.year
sns.displot(data_year)
plt.show()