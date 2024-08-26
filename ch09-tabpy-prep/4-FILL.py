def test(df):
    df['Amount'] = df['Amount'].fillna()
    return df
