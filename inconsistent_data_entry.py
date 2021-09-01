import pandas as pd
import chardet
import fuzzywuzzy
from fuzzywuzzy import process

# detect encoding
with open('dataset/Pakistan Intellectual Capital - Computer Science - Ver 1.csv', 'rb') as raw_data:
    result = chardet.detect(raw_data.read(10000))

print(result)

# read data
data = pd.read_csv('dataset/Pakistan Intellectual Capital - Computer Science - Ver 1.csv', encoding='ISO-8859-1')

# print countries of data
data = data.dropna(subset=['Country'])
countries = data['Country'].unique()
countries.sort()
print('\n', countries)

# remove inconsistent ' New Zealand' and 'New ZeaLand'
data['Country'] = data['Country'].str.lower()
data["Country"] = data['Country'].str.strip()

countries = data['Country'].unique()
countries.sort()
print('\n', countries)

# find the most closet
matches = fuzzywuzzy.process.extract("south korea", countries, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

print('\n', matches)