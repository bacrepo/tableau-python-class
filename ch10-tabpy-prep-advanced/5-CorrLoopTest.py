import pandas as pd
import numpy as np 

df = pd.read_csv("4-ProductDetail.csv")

list_product = df['Product'].unique().tolist()
print(list_product)

list_output = []
for product in list_product:
    df1 = df[df['Product'] == product]
    correlation = np.corrcoef( df1['Sales'], df1['Profit'] )[0][1]
    list_output.append([product, correlation])

df_output = pd.DataFrame(list_output, columns=['Product','Correlation'])
print(df_output)


