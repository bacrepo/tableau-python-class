import pandas as pd
import numpy as np 

def get_output_schema():
    return pd.DataFrame({
		'Product': prep_string(),
		'Correlation': prep_decimal()
    })

def test(df):
    list_output = []
    list_product = df['Product'].unique().tolist()

    for product in list_product:
        df1 = df[df['Product'] == product]
        correlation = np.corrcoef( df1['Sales'], df1['Profit'] )[0][1]
        list_output.append([product, correlation])    
    
    df_output = pd.DataFrame(list_output, columns=['Product','Correlation'])
    return df_output

