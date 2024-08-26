import pandas as pd

df = pd.read_csv("4-ProductDetail.csv")
print(df)

df_corr = df.groupby("Product")[['Sales','Profit']].corr()
print(df_corr)

df_output = pd.DataFrame(df_corr.iloc[0::2,-1]).reset_index()
print(df_output)

df_output = df_output[['Product','Profit']]
df_output.columns = ['Product','Correlation']
print(df_output)

