def test(df):
    df = df.sort_values("RowID", ascending=True)
    df['Amount'] = df['Amount'].fillna(df['Amount'].mean())
    df['AmountShift'] = df['Amount'].shift(1).fillna(0)
    return df