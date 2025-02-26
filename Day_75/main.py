import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def main() -> None:
    df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')
    df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
    df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')
    df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')
    # Challenge:
    # What are the shapes of the dataframes?
    # How many rows and columns?
    # What are the column names?
    # Complete the f-string to show the largest/smallest number in the search data column
    # Try the .describe() function to see some useful descriptive statistics
    # What is the periodicity of the time series data (daily, weekly, monthly)?
    # What does a value of 100 in the Google Trend search popularity actually mean?

    print(f'df_tesla: {df_tesla.shape} {list(df_tesla)}\n'
          f'df_btc_search: {df_btc_search.shape} {list(df_btc_search)}\n'
          f'df_btc_price: {df_btc_price.shape} {list(df_btc_price)}\n'
          f'df_unemployment: {df_unemployment.shape} {list(df_unemployment)}')

    print(f'Largest value for Tesla in Web Search: {df_tesla["TSLA_WEB_SEARCH"].max()}')
    print(f'Smallest value for Tesla in Web Search: {df_tesla["TSLA_WEB_SEARCH"].min()}')
    print('Largest value for "Unemployemnt Benefits" '
          f'in Web Search: {df_unemployment["UE_BENEFITS_WEB_SEARCH"].max()}')
    print(f'Largest BTC News Search: {df_btc_search["BTC_NEWS_SEARCH"].max()}')
    print(f'Tesla describe": \n{df_tesla.describe()}')

    # Challenge: Are there any missing values in any of the dataframes?
    # If so, which row/rows have missing values? How many missing values are there?
    missing: dict[str, int] = {
        'Tesla': int(df_tesla.isna().sum().sum()),
        'U/E': int(df_unemployment.isna().sum().sum()),
        'BTC Search': int(df_btc_search.isna().values.sum()),
        'BTC Price': int(df_btc_price.isna().values.sum())
    }
    print(f'Missing values for Tesla?: {missing["Tesla"]}')
    print(f'Missing values for U/E?: {missing["U/E"]}')
    print(f'Missing values for BTC Search?: {missing["BTC Search"]}')
    print(f'Missing values for BTC price?: {missing["BTC Price"]}')
    print(f'Number of missing values: {sum([value for value in missing.values()])}')

    # Challenge: Remove any missing values that you found.
    df_btc_price.dropna(inplace=True)
    print(df_btc_price.isna().values.sum())

    # Challenge: Check the data type of the entries in the DataFrame MONTH or DATE columns.
    # Convert any strings in to Datetime objects. Do this for all 4 DataFrames.
    # Double check if your type conversion was successful.
    print(type(df_tesla.MONTH[0]))
    df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
    df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
    df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
    df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
    print(type(df_tesla.MONTH[0]))

    df_btc_monthly = df_btc_price.resample('ME', on='DATE').last()
    print(df_btc_monthly)

    matplotlib.use('TkAgg')
    years = mdates.YearLocator()
    months = mdates.MonthLocator()
    years_fmt = mdates.DateFormatter('%Y')
    # plt.figure(figsize=(14, 8), dpi=120)
    # plt.title('Tesla Web Search vs Price', fontsize=18)
    # ax1 = plt.gca()
    # ax2 = ax1.twinx()
    # ax1.xaxis.set_major_locator(years)
    # ax1.xaxis.set_major_formatter(years_fmt)
    # ax1.xaxis.set_minor_locator(months)
    # ax1.set_ylabel('TSLA Stock Price', color='cyan', fontsize=14)
    # ax2.set_ylabel('Search Trend', color='#ff5733', fontsize=14)
    # ax1.plot(df_tesla["MONTH"], df_tesla["TSLA_USD_CLOSE"], color='cyan', linewidth=3)
    # ax2.plot(df_tesla["MONTH"], df_tesla["TSLA_WEB_SEARCH"], color='#ff5733', linewidth=3)
    # plt.show()

    # plt.figure(figsize=(14, 8), dpi=120)
    # plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
    # plt.xticks(fontsize=14, rotation=45)
    # ax1 = plt.gca()
    # ax2 = ax1.twinx()
    # ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
    # ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
    # ax1.xaxis.set_major_locator(years)
    # ax1.xaxis.set_major_formatter(years_fmt)
    # ax1.xaxis.set_minor_locator(months)
    # ax1.set_ylim(bottom=0, top=15000)
    # ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
    # # Experiment with the linestyle and markers
    # ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE,
    #          color='#F08F2E', linewidth=3, linestyle='--')
    # ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH,
    #          color='skyblue', linewidth=3, marker='o')
    # plt.show()

    # plt.figure(figsize=(14, 8), dpi=120)
    # plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
    # plt.yticks(fontsize=14)
    # plt.xticks(fontsize=14, rotation=45)
    #
    # ax1 = plt.gca()
    # ax2 = ax1.twinx()
    #
    # ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
    # ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
    #
    # ax1.xaxis.set_major_locator(years)
    # ax1.xaxis.set_major_formatter(years_fmt)
    # ax1.xaxis.set_minor_locator(months)
    #
    # ax1.set_ylim(bottom=3, top=10.5)
    # ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
    #
    # # Show the grid lines as dark grey lines
    # ax1.grid(color='grey', linestyle='--')
    # roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
    #
    # # Change the dataset used
    # ax1.plot(df_unemployment.MONTH, roll_df.UNRATE,
    #          color='purple', linewidth=3, linestyle='--')
    # ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH,
    #          color='skyblue', linewidth=3)
    #
    # plt.show()

    df_ue_2020 = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-20.csv')
    df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)
    plt.figure(figsize=(14, 8), dpi=120)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14, rotation=45)
    plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
    ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

    ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])

    ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, 'purple', linewidth=3)
    ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

    plt.show()


if __name__ == '__main__':
    main()
