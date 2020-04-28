import pandas as pd
import googlemaps
from itertools import tee

#Read CSV file into dataframe named 'df'
#change seperator (sep e.g. ',') type if necessary
df = pd.read_csv("PizzaEssentials.csv")

#Perform request to use the Google Maps API web service
API_key = 'AIzaSyAyTUcgbuwbey0p5n5q6BK-PMGHAoAgiJg'#enter Google Maps API key
gmaps = googlemaps.Client(key=API_key)


#use pairwise function to be used to iterate through two consecutive rows (pairs) in a data frame
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

#empty list - will be used to store calculated distances
list = [0]

# Loop through each row in the data frame using pairwise
for (i1, row1), (i2, row2) in pairwise(df.iterrows()):
      #Assign latitude and longitude as origin/departure points
      LatOrigin = row1['Latitude']
      LongOrigin = row1['Longitude']
      origins = (LatOrigin,LongOrigin)

      #Assign latitude and longitude from the next row as the destination point
      LatDest = row2['Latitude']   # Save value as lat
      LongDest = row2['Longitude']  # Save value as lat
      destination = (LatDest,LongDest)

      #pass origin and destination variables to distance_matrix function# output in meters
      result = gmaps.distance_matrix(origins, destination, mode='walking')["rows"][0]["elements"][0]["distance"]["value"]

      #append result to list
      list.append(result)

#Add column 'Distance' to data frame and assign to list values
df['Distance'] = list

df.to_csv('calculated_distances.csv', index=None)