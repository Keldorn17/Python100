import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


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


if __name__ == '__main__':
    main()
