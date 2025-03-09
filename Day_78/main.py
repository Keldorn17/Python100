import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def main() -> None:
    matplotlib.use('TkAgg')

    pd.options.display.float_format = '{:,.2f}'.format

    from pandas.plotting import register_matplotlib_converters
    register_matplotlib_converters()

    data = pd.read_csv('cost_revenue_dirty.csv')

    print(data.shape)
    print(data.isna().values.any())
    print(data.duplicated().values.any())
    duplicated_rows = data[data.duplicated()]
    print(len(duplicated_rows))
    print(data.info())

    chars_to_remove = [',', '$']
    columns_to_clean = ['USD_Production_Budget',
                        'USD_Worldwide_Gross',
                        'USD_Domestic_Gross']

    for col in columns_to_clean:
        for char in chars_to_remove:
            data[col] = data[col].astype(str).str.replace(char, "")
        data[col] = pd.to_numeric(data[col])

    data.Release_Date = pd.to_datetime(data.Release_Date)

    print(f"Average Production Budget: ${round(data['USD_Production_Budget'].mean()):,}")
    print(f"Average Gross Revenue Worldwide: ${round(data['USD_Worldwide_Gross'].mean()):,}")
    print(f"Min Gross Revenue Worldwide: ${round(data['USD_Worldwide_Gross'].min()):,}")
    print(f"Min Gross Revenue Domestic: ${round(data['USD_Domestic_Gross'].min()):,}")
    print(data.describe())
    print(f"Max Gross Revenue Wordwide: ${round(data['USD_Worldwide_Gross'].max()):,}")
    print(f"Max Gross Revenue Domestic: ${round(data['USD_Domestic_Gross'].max()):,}")

    print(f"Number of films with $0 domestic gross revenue: {len(data[data['USD_Domestic_Gross'] == 0])}")
    print(f"Number of films with $0 worldwide gross revenue: {len(data[data['USD_Domestic_Gross'] == 0])}")

    international_releases = data.loc[(data.USD_Domestic_Gross == 0) &
                                      (data.USD_Worldwide_Gross != 0)]
    international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')

    scrape_date = pd.Timestamp('2018-5-1')
    future_release = data[data.Release_Date >= scrape_date]
    print(f"Number of unreleased movies: {len(future_release)}")

    data_clean = data.drop(future_release.index)

    losing_money = data.query('USD_Production_Budget > USD_Worldwide_Gross')
    print(f"{round(len(losing_money) / len(data) * 100, 2)}% of the films lost money.")

    # plt.figure(figsize=(8, 4), dpi=200)
    #
    # # set styling on a single chart
    # with sns.axes_style('darkgrid'):
    #     ax = sns.scatterplot(data=data_clean,
    #                          x='USD_Production_Budget',
    #                          y='USD_Worldwide_Gross',
    #                          hue='USD_Worldwide_Gross',
    #                          size='USD_Worldwide_Gross')
    #
    #     ax.set(ylim=(0, 3000000000),
    #            xlim=(0, 450000000),
    #            ylabel='Revenue in $ billions',
    #            xlabel='Budget in $100 millions')
    #     plt.show()

    # plt.figure(figsize=(8, 4), dpi=200)
    #
    # with sns.axes_style("darkgrid"):
    #     ax = sns.scatterplot(data=data_clean,
    #                          x='Release_Date',
    #                          y='USD_Production_Budget',
    #                          hue='USD_Worldwide_Gross',
    #                          size='USD_Worldwide_Gross', )
    #
    #     ax.set(ylim=(0, 450000000),
    #            xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
    #            xlabel='Year',
    #            ylabel='Budget in $100 millions')
    #     plt.show()

    dt_index = pd.DatetimeIndex(data_clean.Release_Date)
    years = dt_index.year
    decades = years // 10 * 10
    data_clean['Decade'] = decades

    old_films = data_clean[data_clean.Decade <= 1960]
    new_films = data_clean[data_clean.Decade > 1960]

    # plt.figure(figsize=(8, 4), dpi=200)
    # with sns.axes_style("whitegrid"):
    #     sns.regplot(data=old_films,
    #                 x='USD_Production_Budget',
    #                 y='USD_Worldwide_Gross',
    #                 scatter_kws={'alpha': 0.4},
    #                 line_kws={'color': 'black'})
    #     plt.show()

    # plt.figure(figsize=(8, 4), dpi=200)
    # with sns.axes_style('darkgrid'):
    #     ax = sns.regplot(data=new_films,
    #                      x='USD_Production_Budget',
    #                      y='USD_Worldwide_Gross',
    #                      color='#2f4b7c',
    #                      scatter_kws={'alpha': 0.3},
    #                      line_kws={'color': '#ff7c43'})
    #
    #     ax.set(ylim=(0, 3000000000),
    #            xlim=(0, 450000000),
    #            ylabel='Revenue in $ billions',
    #            xlabel='Budget in $100 millions')
    #     plt.show()


if __name__ == '__main__':
    main()
