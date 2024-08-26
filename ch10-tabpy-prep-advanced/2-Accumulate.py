def test(df):
    df_group = df.groupby(['Segment','Year','YearMonth'])['Sales'].sum().reset_index()
    df_group = df_group.sort_values(['Segment','Year','YearMonth'])
    df_group['SalesYTD'] = df_group.groupby(['Segment','Year'])['Sales'].apply(lambda x: x.cumsum())
    return df_group
