import pandas as pd
from prophet import Prophet
df = pd.read_csv('SalesSummary.csv')

print(df)
df1 = df[['TransDate','Sales']]
df1.columns = ['ds','y']

f = Prophet()
f.fit(df1)
print(f)

