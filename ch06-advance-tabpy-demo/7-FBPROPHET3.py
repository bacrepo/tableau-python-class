import pandas as pd
from prophet import Prophet

df = pd.read_csv('SalesSummary.csv')
df1 = df[['TransDate','Sales']]
df1.columns = ['ds','y']
print(df1)

f = Prophet()
f.fit(df1)

future_days = 100
future = f.make_future_dataframe(periods=future_days)
forecast = f.predict(future)

df2 = forecast[['ds','yhat']]
print(df2)

df2.to_csv('SalesSummaryForecast.csv', index=False)

