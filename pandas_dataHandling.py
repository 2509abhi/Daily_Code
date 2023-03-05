# df = pd.read_csv('C:\\Users\\Abhishek\\OneDrive\\Desktop\\college usar\\SampleData.csv')
import pandas as pd
import numpy as np
import xlrd as xl
import openpyxl
df = pd.read_csv('C:\\Users\\Abhishek\\OneDrive\\Desktop\\college usar\\SampleData.csv',na_values=['-1'])
print(df.day)
df = df.set_index('day')
print(df)
ndf = df.fillna({
    'temperature': 0,
    'widespread': 0,
    'event' : 'No Detail'
})
print(ndf)
fdf = df.fillna(method = 'ffill')
print(fdf)
bdf = df.fillna(method = 'bfill')
print(bdf)

