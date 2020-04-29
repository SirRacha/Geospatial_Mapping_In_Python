import pandas as pd
import googlemaps
from itertools import tee

# Read CSV file into dataframe named 'df'
# change seperator (sep e.g. ',') type if necessary
df = pd.read_csv("../data/PizzaEssentials.csv"

# Perform request to use the Google Maps API web service
API_key='API_KEY'  # enter Google Maps API key
gmaps=googlemaps.Client(key=API_key)


# use pairwise function to be used to iterate through two consecutive rows (pairs) in a data frame
def pairwise(iterable):
    a, b=tee(iterable)
    next(b, None)
    return zip(a, b)


# empty list - will be used to store calculated distances
list=[0]

# Loop through each row in the data frame using pairwise
for (i1, row1), (i2, row2) in pairwise(df.iterrows()):
    # Assign latitude and longitude as origin/departure points

    origins=40.70258, -73.9932403 | 40.79715, -73.93488 | 40.59474, -73.9813 | 40.723009999999995, -73.99459 | 40.854209999999995, -73.88825 | 40.85457, -73.88823000000001 | 40.85479, -73.88795999999999 | 40.66165, -73.99338 | 40.75458, -73.98697 | 40.70492, -73.93401999999999 | 40.731640000000006, -74.00335 | 40.57891, - \
        73.98382 | 40.72157, -73.99568000000001 | 40.71907, -73.99708000000001 | 40.625009999999996, -73.96154 | 40.75565, -73.99421 | 40.70898, - \
        73.83053000000001 | 40.853559999999995, -73.88902 | 40.854209999999995, - \
        73.88825 | 40.69985, -73.83279 | 40.85555, - \
        73.88757 | 40.71561, -73.95347 | 40.6818, -74.00029

    # Assign latitude and longitude from the next row as the destination point

    destination=40.70258, -73.9932403 | 40.79715, -73.93488 | 40.59474, -73.9813 | 40.723009999999995, -73.99459 | 40.854209999999995, -73.88825 | 40.85457, -73.88823000000001 | 40.85479, -73.88795999999999 | 40.66165, -73.99338 | 40.75458, -73.98697 | 40.70492, -73.93401999999999 | 40.731640000000006, -74.00335 | 40.57891, - \
        73.98382 | 40.72157, -73.99568000000001 | 40.71907, -73.99708000000001 | 40.625009999999996, -73.96154 | 40.75565, -73.99421 | 40.70898, - \
        73.83053000000001 | 40.853559999999995, -73.88902 | 40.854209999999995, - \
        73.88825 | 40.69985, -73.83279 | 40.85555, - \
        73.88757 | 40.71561, -73.95347 | 40.6818, -74.00029

    # pass origin and destination variables to distance_matrix function# output in meters
    result=gmaps.distance_matrix(origins, destination, mode='driving')[
        "rows"][0]["elements"][0]["distance"]["value"]

    # append result to list
    list.append(result)

# Add column 'Distance' to data frame and assign to list values
df['Distance']=list

df.to_csv('..data/Test.csv', index=None)
