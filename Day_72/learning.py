import pandas


def main() -> None:
    data_frame = pandas.read_csv('salaries_by_college_major.csv')
    # print(data_frame.head())
    # print(data_frame.shape)
    # print(data_frame.columns)
    # print(data_frame.isna())
    # print(data_frame.tail())
    clean_df = data_frame.dropna()
    print(clean_df.tail())
    print(clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmax()])

    print(clean_df['Mid-Career Median Salary'].max())
    print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
    print(clean_df['Undergraduate Major'][clean_df['Mid-Career Median Salary'].idxmax()])

    print(clean_df['Starting Median Salary'].min())
    print(clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()])

    spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
    clean_df.insert(1, 'Spread', spread_col)
    print(clean_df.head())

    low_risk = clean_df.sort_values('Spread')
    print(low_risk[['Undergraduate Major', 'Spread']].head())

    highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
    print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

    highest_spread = clean_df.sort_values('Spread', ascending=False)
    print(highest_spread[['Undergraduate Major', 'Spread']].head())

    print(clean_df.groupby('Group').count())

    pandas.options.display.float_format = '{:,.2f}'.format


if __name__ == '__main__':
    main()
