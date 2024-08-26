import pandas as pd

def get_output_schema():
    return pd.DataFrame({
		'Product': prep_string(),
		'Correlation': prep_decimal()
    })

def test(df):
    df_corr = df.groupby("Product")[['Sales','Profit']].corr()
    df_output = pd.DataFrame(df_corr.iloc[0::2,-1]).reset_index()
    df_output = df_output[['Product','Profit']]
    df_output.columns = ['Product','Correlation']  
    return df_output

