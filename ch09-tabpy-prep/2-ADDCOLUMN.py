import pandas as pd

def get_output_schema():
    return pd.DataFrame({
		'RowID': prep_int(),
		'Gender': prep_string(),
		'Name': prep_string(),		
		'Amount': prep_decimal(),
		'Cost': prep_decimal()
    })

def test(df):
    df['Cost'] = df['Amount'] * 0.7
    return df

