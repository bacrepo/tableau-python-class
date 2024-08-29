import pandas as pd
from prophet import Prophet

df_input = pd.read_csv("3-SalesSummary.csv")
df_input = df_input[['TransDate', 'Sales']]
df_input.columns = ['ds', 'y']
print(df_input)
df = df_input

days = 100
f = Prophet()
f.fit(df)
future = f.make_future_dataframe(periods=days)
forecast = f.predict(future)
df_output = forecast[['ds', 'yhat']]
print(df_output)
