def test(df):
    df['Amount'] = df['Amount'].fillna(df.groupby('Gender')['Amount'].transform('mean'))
    return df
