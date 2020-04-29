import pandas
import numpy as np
import math
import numpy
from sklearn.metrics.pairwise import euclidean_distances
from haversine import haversine, Unit
from scipy.spatial import distance

print("STARTING PROGRAM")

# to make integers, change haversine to miles, * 100 to make all integers, then run on google TSP again

# Define Euclidean Distance formula
#from math import dist


def euclidean(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    # return np.sqrt(np.sum((coord1-coord2)**2))
    # return euclidean_distances([x1np], [x2np])
    return spatial.distance.euclidean(coord1, coord2)


def haversine_manual(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2

    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))


if __name__ == '__main__':

    pizza_df = pandas.read_csv('../data/PizzaEssentials_Reduced.csv')

    # Get the values from the dataframe
    ndarray_values = pizza_df.values

    # create a matrix
    # using np.zeros creates a matrix and -- as used here -- fills it with zeros the size given by parameters
    my_matrix = np.zeros((len(ndarray_values), len(ndarray_values)))

    # Loop - these variables contain (index, (longitude, latitude))
    # We will calculate the distance between every point to every other point
    for outer_idx, outer_var in enumerate(ndarray_values[0:, 0:2]):

        # Loop - these variables contain (index, (longitude, latitude))
        for inner_idx, inner_var in enumerate(ndarray_values[0:, 0:2]):

            # calculate dist from outer_var to each inner_var and add to matrix
            # multiply by 100 to increase size of values to make all integers for TSP calculation
            # FOR HAVERSINE
            my_matrix[outer_idx][inner_idx] = haversine(
                outer_var, inner_var) * 1000
            # FOR EUCLIDEAN
            # my_matrix[outer_idx][inner_idx] = euclidean(outer_var, inner_var, unit='mi') * 1000
            # FOR MANHATTAN
            #my_matrix[outer_idx][inner_idx] = distance.cdist(outer_var, inner_var, 'cityblock') * 1000

    # Save results to file
    # Make sure to change name of output file depending on choes distance calculation ABOVE
    # , columns={'Longitude','Latitude','Name','Comment','URL'})
    results_dataframe = pandas.DataFrame(my_matrix)

    results_dataframe.to_csv("../data/test5.csv")

    print("Done")
