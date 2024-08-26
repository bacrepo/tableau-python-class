def test(df):
    df['Rank'] = df.groupby('Year')['AmountUSD'].rank(ascending=False)
    df = df[df['Rank'] <= 15]
    return df
