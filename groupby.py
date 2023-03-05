import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\Abhishek\\OneDrive\\Desktop\\college usar\\SampleData.csv')
print(df)
nwdf = df.groupby('city')
# print(nwdf['mumbai'])
for city , citydf in nwdf:
    print(city)
    print(citydf)
print(nwdf.max())
print(nwdf.describe())
