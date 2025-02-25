import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def main() -> None:
    # Challenge: How many different colours does the LEGO company produce?
    # Read the colors.csv file in the data folder and find the total number of unique colours.
    # Try using the .nunique() method to accomplish this
    lego_df = pd.read_csv('data/colors.csv')
    print(f'Unique colors: {lego_df.nunique()['name']}')

    print(f'First Solution: Number of transparent colors: {lego_df.groupby("is_trans").count()["id"].iloc[1]}')
    print(f'Second Solution: Number of transparent colors: {lego_df["is_trans"].value_counts()["t"]}')

    # The sets.csv data contains a list of sets over the years
    # and the number of parts that each of these sets contained.
    # Challenge: Read the sets.csv data and take a look at the first and last couple of rows.
    sets_df = pd.read_csv('data/sets.csv')
    # print(sets_df.head())
    # print(sets_df.tail())
    # Challenge: In which year were the first LEGO sets released and what were these sets called?
    sorted_sets = sets_df.sort_values("year")
    starting_year = sorted_sets.iloc[0]["year"]
    print(f'First Solution: First lego sets release year: {starting_year}')
    print(f'Second Solution: First lego sets release year: {sets_df.min()["year"]}')
    print(f'Third Solution: First lego sets release year: {sets_df[sets_df['year'] == 1949]}')

    # Challenge: How many different sets did LEGO sell in their first year?
    # How many types of LEGO products were on offer in the year the company started?
    print(f'First year lego sets count: {sets_df["year"].value_counts().get(starting_year)}')
    # Challenge: Find the top 5 LEGO sets with the most number of parts.
    print(f'Top 5 LEGO sets with the most number of parts: \n'
          f'{sets_df.sort_values("num_parts", ascending=False).head()}')

    sets_by_year = sets_df.groupby('year').count()['set_num']
    print(sets_by_year.head())
    # plt.plot(sets_by_year.index[:-2], sets_by_year[:-2])
    # plt.show()

    themes_by_year = sets_df.groupby('year').agg({'theme_id': pd.Series.nunique})
    themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
    print(themes_by_year.head())

    # plt.plot(themes_by_year.index[:-2], themes_by_year[:-2])

    # ax1 = plt.gca()  # get current axes
    # ax2 = ax1.twinx()
    # ax1.plot(sets_by_year.index[:-2], sets_by_year[:-2], color='g')
    # ax2.plot(themes_by_year.index[:-2], themes_by_year[:-2], color='b')
    # ax1.set_xlabel('Year')
    # ax1.set_ylabel('Number of Sets', color='green')
    # ax2.set_ylabel('Number of Themes', color='blue')
    # plt.show()

    parts_per_set = sets_df.groupby('year').agg({'num_parts': pd.Series.mean})
    print(parts_per_set.head())
    # plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
    # plt.show()

    set_theme_count = sets_df['theme_id'].value_counts()
    print(set_theme_count[:5])

    themes_df = pd.read_csv('data/themes.csv')
    star_wars_ids = [ids for ids in themes_df[themes_df['name'] == 'Star Wars']['id']]
    for sw_id in star_wars_ids:
        print(sets_df[sets_df['theme_id'] == sw_id])

    set_theme_count = pd.DataFrame({
        'id': set_theme_count.index,
        'set_count': set_theme_count.values
    })
    print(set_theme_count.head())
    merged_df = pd.merge(set_theme_count, themes_df, on='id')
    print(merged_df[:3])
    plt.figure(figsize=(14, 8))
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.ylabel('Nr of Sets', fontsize=14)
    plt.xlabel('Theme Name', fontsize=14)
    plt.bar(merged_df.name[:10], merged_df.set_count[:10])
    plt.show()


if __name__ == '__main__':
    main()
