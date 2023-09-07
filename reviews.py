# add your code here
# make a python prpgram that thats reads data/winemag-data-130k.v2.csv.zip
# create a summary that contains name, numbers of reviews and the average points for each unique country in the dataset 
# write the summary data to a new file in the data folder named reviews-per-country.csv
#import pandas as pd

# Read the CSV file
#df = pd.read_csv('data/winemag-data-130k-v2.csv')

# Group the data by country, calculate the number of reviews and average points
#ummary_data = df.groupby('country').agg({'country': 'count', 'points': 'mean'}).rename(columns={'country': 'count', 'points': 'average_points'}).reset_index()

# Round the 'average_points' column to 1 decimal point
#summary_data['average_points'] = summary_data['average_points'].round(1)

# Sort the summary data by country
#summary_data = summary_data.sort_values(by='country')

# Slice the summary_data DataFrame to select only the first five and last five rows
#top_and_bottom_countries = pd.concat([summary_data.head(5), summary_data.tail(5)])

# Save the selected summary data to a new CSV file in the 'data' folder
#top_and_bottom_countries.to_csv('data/reviews-per-country.csv', index=False)

#print("Summary data for the top and bottom countries saved to data/reviews-per-country.csv")
import pandas as pd 
import zipfile


df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', index_col=0)

wine_df = df
wine_df['count'] = 1

review_av = wine_df.groupby('country').agg({'count': 'sum', 'points': 'mean'}).reset_index()
review_av['points'] = review_av['points'].round(1)
sorted_reviews = review_av.sort_values(by='count', ascending=True)

sorted_reviews.to_csv('data/reviews-per-country.csv', index=False)


