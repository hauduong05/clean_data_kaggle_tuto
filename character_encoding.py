import pandas as pd
import numpy as np
import chardet

before = "This is the euro symbol: €"

# encode and decode in utf-8
after_utf = before.encode(encoding='utf-8', errors='replace')
print(after_utf)
print(after_utf.decode('utf-8'))

# encode and decode in ascii
after_ascii = before.encode('ascii', errors='replace')
print(after_ascii)
print(after_ascii.decode('ascii'))

# kickstarter_data = pd.read_csv('dataset/ks-projects-201612.csv') false because encoding not utf-8

# detect encoding
with open('dataset/ks-projects-201612.csv', 'rb') as raw_data:
    result = chardet.detect(raw_data.read(1000))

print(result)

# read data with encoding
ks_data = pd.read_csv('dataset/ks-projects-201612.csv', encoding='Windows-1252')
print(ks_data.head())

# save file in utf-8 encoding
ks_data.to_csv('ks_data_utf_8.csv')