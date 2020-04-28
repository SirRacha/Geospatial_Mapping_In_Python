import pandas
import numpy as np

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

    # Tuple of 2 series variables
    #series_lon_lat = (pizza_df['Longitude'], pizza_df['Latitude'])
    ndarray_values = pizza_df.values
   
    # create a matrix
    my_matrix = np.zeros((len(ndarray_values), len(ndarray_values)))
   
    for outer_idx, outer_var in enumerate(ndarray_values[0:,0:2]):
         
        for inner_idx, inner_var in enumerate(ndarray_values[0:,0:2]):
           
            # calculate dist from outer_var to each inner_var
            d = calculate_dist(outer_var, inner_var)
           
            # add to matrix
            my_matrix[outer_idx][inner_idx] = d
   
    print("Done")

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

df.to_csv('calculated_distances5.csv', index=None)
      
'''    
# driver code  
lat1 = 53.32055555555556
lat2 = 53.31861111111111
lon1 = -1.7297222222222221
lon2 =  -1.6997222222222223
print(distance(lat1, lat2, lon1, lon2), "K.M") 
'''

'''
if __name__ == '__main__':

    pizza_df = pandas.read_csv('PizzaEssentials.csv')
   
    # Tuple of 2 series variables
    #series_lon_lat = (pizza_df['Longitude'], pizza_df['Latitude'])
    ndarray_values = pizza_df.values
   
    # create a matrix
    my_matrix = np.zeros((len(ndarray_values), len(ndarray_values)))
   
    for outer_idx, outer_var in enumerate(ndarray_values[0:,0:2]):
         
        for inner_idx, inner_var in enumerate(ndarray_values[0:,0:2]):
           
            # calculate dist from outer_var to each inner_var
            d = calculate_dist(outer_var, inner_var)
           
            # add to matrix
            my_matrix[outer_idx][inner_idx] = d
   
    print("Done")
'''