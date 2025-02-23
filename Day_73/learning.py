import pandas
import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')

# Challenge: Read the .csv file and store it in a Pandas dataframe
df = pandas.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
# Challenge: Examine the first 5 rows and the last 5 rows of the of the dataframe
print(df.head())
print(df.tail())
# Challenge: Check how many rows and how many columns there are. What are the dimensions of the dataframe?
print(df.shape)
# Challenge: Count the number of entries in each column of the dataframe
print(df.count())

# Challenge: Calculate the total number of post per language. Which Programming language has had
# the highest total number of posts of all time?
print(df.groupby('TAG').sum().idxmax()['POSTS'])

# Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in September 2008.
# Challenge: How many months of data exist per language? Which language had the fewest months with an entry?
print(df.groupby('TAG').count().idxmin()['POSTS'])

df.DATE = pandas.to_datetime(df['DATE'])
print(df.head())

test_df = pandas.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                            'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                            'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
print(test_df)
pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivoted_df)

# Challenge: What are the dimensions of our new dataframe? How many rows and columns does it have?
# Print out the column names and print out the first 5 rows of the dataframe.
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True)
print(reshaped_df.isna().values.any())
print(reshaped_df.shape)
print(reshaped_df.columns)
print(reshaped_df.head())

# Challenge: Count the number of entries per programming language. Why might the number of entries be different?
print(reshaped_df.count())

# plt.figure(figsize=(12, 8))
# plt.xlabel('Date', fontsize=12)
# plt.ylabel('Number of Posts', fontsize=12)
# plt.ylim(0, 35000)
# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column],
#              linewidth=3, label=reshaped_df[column].name)
# plt.legend(fontsize=12)
# plt.show()

roll_df = reshaped_df.rolling(window=12).mean()

plt.figure(figsize=(12, 8))
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Posts', fontsize=12)
plt.ylim(0, 35000)
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)
plt.legend(fontsize=12)
plt.show()
