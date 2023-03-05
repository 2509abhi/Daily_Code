import pandas as pd
import numpy as np
# import xlrd as xl
# import openpyxl
df = pd.read_csv('C:\\Users\\Abhishek\\OneDrive\\Desktop\\college usar\\SampleData.csv',na_values=['-1'])
df.day= pd.to_datetime(df.day, infer_datetime_format=True)
print(df.day)
print(type(df.day[0]))
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
bdf = df.fillna(method = 'ffill', limit=1)
print(bdf)
# new_df = df.interpolate(mathod = "pad")
# print(new_df.day)
dt = pd.date_range('2017-02-02','02-02-2018')
idx = pd.DatetimeIndex(dt)
print(df.reindex(idx))

print(df)
print(df.replace({
    'temperature': 32,
    'widespread': 7,
    'event': 'NaN'
},np.nan))
print(df.replace({
    '28': 32,
    'widespread': 7,
    'event': 'NaN'
}))
