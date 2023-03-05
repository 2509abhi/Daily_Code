import pandas as pd
df = pd.DataFrame({
    'a': [1,2,3,4,5,6],
    'b': [1,2.5,4.6,5.6,6.7,7.9]
})
df2 = pd.DataFrame({
    'a': [1,2,3,4],
    'b': [1.12,2.52,4.61,5.64]
})
s = pd.Series((1,10))
df3 = pd.concat([df,df2,s], axis=1)
print(df3)
df3 = pd.concat([df,df2], axis=0)
print(df3)
df3 = pd.merge(df,df2, on="a", suffixes=("daf","daa"), how="left")
print(df3)
