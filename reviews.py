# add your code here
# make a python prpgram that thats reads data/winemag-data-130k.v2.csv.zip
# create a summary that contains name, numbers of reviews and the average points for each unique country in the dataset 
# write the summary data to a new file in the data folder named reviews-per-country.csv
import pandas as pd
import zipfile


with zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as zip_ref:
    zip_ref.extractall('data')


df = pd.read_csv('data/winemag-data-130k-v2.csv')

# Group the data by country, calculate the number of reviews and average points
summary_data = df.groupby('country').agg({'country': 'count', 'points': 'mean'}).rename(columns={'country': 'count', 'points': 'average_points'}).reset_index()


summary_data['average_points'] = summary_data['average_points'].round(1)


summary_data = summary_data.sort_values(by='country')


summary_data.to_csv('data/reviews-per-country.csv', index=False)

print("Summary data saved to data/reviews-per-country.csv")




