import pandas as pd
import plotly.express as px

pd.options.display.float_format = '{:,.2f}'.format
df_apps = pd.read_csv('apps.csv')

# Challenge: How many rows and columns does df_apps have?
# What are the column names? Look at a random sample of 5 different rows with .sample().

print(df_apps.shape)
print(df_apps.sample(5))

# Challenge: Remove the columns called Last_Updated and Android_Version from the DataFrame.
# We will not use these columns.
df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)

# Challenge: How may rows have a NaN value (not-a-number) in the Ratings column?
# Create DataFrame called df_apps_clean that does not include these rows.
print(df_apps.isna().sum())
df_apps_clean = df_apps.dropna()

# Challenge: Are there any duplicates in data? Check for duplicates using the .duplicated() function.
# How many entries can you find for the "Instagram" app?
# Use .drop_duplicates() to remove any duplicates from df_apps_clean.

print(df_apps_clean.duplicated())
print(df_apps_clean[df_apps_clean['App'] == 'Instagram'])
df_apps_clean = df_apps_clean.drop_duplicates()

# Challenge: Identify which apps are the highest rated.
# What problem might you encounter if you rely exclusively on ratings alone to determine the quality of an app?
print(df_apps_clean.sort_values('Rating', ascending=False).head())

# Challenge: What's the size in megabytes (MB) of the largest Android apps in the Google Play Store.
# Based on the data, do you think there could be limit in place or can developers make apps as large as they please?

print(df_apps_clean.sort_values('Size_MBs', ascending=False).head())

# Challenge: Which apps have the highest number of reviews? Are there any paid apps among the top 50?

print(df_apps_clean.sort_values('Reviews', ascending=False).head())
for index, app in enumerate(df_apps_clean.sort_values('Reviews', ascending=False).values):
    if index == 50:
        print('No paid app found in the top 50')
        break
    if app[6] == 'Paid':
        print('Found paid apps in the top 50.')
        break

ratings = df_apps_clean.Content_Rating.value_counts()

# fig = px.pie(labels=ratings.index, values=ratings.values, title='Content Rating', names=ratings.index, hole=0.6)
# fig.update_traces(textposition='outside', textinfo='percent+label')
# fig.show()

# Challenge: How many apps had over 1 billion (that's right - BILLION) installations?
# How many apps just had a single install?
# Check the datatype of the Installs column.
# Count the number of apps at each level of installations.
# Convert the number of installations (the Installs column) to a numeric data type.
# Hint: this is a 2-step process. You'll have make sure you remove non-numeric characters first.

print(df_apps_clean.Installs.describe())
print(df_apps_clean.info())
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
print(df_apps_clean[['App', 'Installs']].groupby('Installs').count())

# Find the Most Expensive Apps, Filter out the Junk, and Calculate a (ballpark) Sales Revenue Estimate
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)

print(df_apps_clean.sort_values('Price', ascending=False).head(20))

# The most expensive apps sub $250
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
print(df_apps_clean.sort_values('Price', ascending=False).head(5))

# Highest Grossing Paid Apps (ballpark estimate)
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
print(df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10])

top10_category = df_apps_clean.Category.value_counts()[:10]
print(top10_category)

# bar = px.bar(x=top10_category.index,  # index = category name
#              y=top10_category.values)
# bar.show()

category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)
#
# h_bar = px.bar(x=category_installs.Installs,
#                y=category_installs.index,
#                orientation='h')
# h_bar.show()

cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
print(cat_merged_df.sort_values('Installs', ascending=False))

# scatter = px.scatter(cat_merged_df,  # data
#                      x='App',  # column name
#                      y='Installs',
#                      title='Category Concentration',
#                      size='App',
#                      hover_name=cat_merged_df.index,
#                      color='Installs')
#
# scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
#                       yaxis_title="Installs",
#                       yaxis=dict(type='log'))
#
# scatter.show()

# Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')

# bar = px.bar(x=num_genres.index[:15],  # index = category name
#              y=num_genres.values[:15],  # count
#              title='Top Genres',
#              hover_name=num_genres.index[:15],
#              color=num_genres.values[:15],
#              color_continuous_scale='Agsunset')
#
# bar.update_layout(xaxis_title='Genre',
#                   yaxis_title='Number of Apps',
#                   coloraxis_showscale=False)
#
# bar.show()

df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
df_free_vs_paid.head()

# g_bar = px.bar(df_free_vs_paid,
#                x='Category',
#                y='App',
#                title='Free vs Paid Apps by Category',
#                color='Type',
#                barmode='group')
#
# g_bar.update_layout(xaxis_title='Category',
#                     yaxis_title='Number of Apps',
#                     xaxis={'categoryorder': 'total descending'},
#                     yaxis=dict(type='log'))
#
# g_bar.show()

# box = px.box(df_apps_clean,
#              y='Installs',
#              x='Type',
#              color='Type',
#              notched=True,
#              points='all',
#              title='How Many Downloads are Paid Apps Giving Up?')
#
# box.update_layout(yaxis=dict(type='log'))
#
# box.show()

df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
# box = px.box(df_paid_apps,
#              x='Category',
#              y='Revenue_Estimate',
#              title='How Much Can Paid Apps Earn?')
#
# box.update_layout(xaxis_title='Category',
#                   yaxis_title='Paid App Ballpark Revenue',
#                   xaxis={'categoryorder': 'min ascending'},
#                   yaxis=dict(type='log'))
#
# box.show()

print(df_paid_apps.Price.median())

box = px.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder': 'max descending'},
                  yaxis=dict(type='log'))

box.show()