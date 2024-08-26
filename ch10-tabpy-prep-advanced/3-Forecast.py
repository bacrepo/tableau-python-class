import pandas as pd
from fbprophet import Prophet

def get_output_schema():
    return pd.DataFrame({
		'ds': prep_date(),
		'yhat': prep_decimal()
    })


def test(df_input):
    
    df = df_input[['ds','y']]
    df['ds'] = df['ds'].astype('str').str.replace("Z","")
    df['ds'] = pd.to_datetime(df['ds'])

    f = Prophet()
    f.fit(df)
    future = f.make_future_dataframe(periods=100)
    forecast = f.predict(future)
    df_output = forecast[['ds','yhat']]

    df_output['ds'] = pd.to_datetime(df_output['ds']).dt.strftime('%Y-%m-%d')

    return df_output
