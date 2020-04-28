# GEOmapping in Python
An exploration into working with geospatial data, transforming data types, and visualizing geospatial data in a multitude of ways.  

## Online and Offline Access
This project includes methods to work with data whether online and offline. Certain business sectors do not have free access to the internet, or control over their machinces and softeware oinstalls. This project provides a few workarounds for these business sectors.

## Data
All data used here is open source.  
	1) NYC Restaurants - DOHMH New York City Restaurant Inspection Results. Has 400,000 restarant locations!  It provides restaurant inspections, violations, grades and adjudication information. It can be found at the New York City's official mapping site. Who knew they had one, but they do! This is a very useful site to get lots of data. They also have shapefiles if you prefer. You need to download this dataset becuase of its size (163mb)
	https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j

		a)  I further curated this dataset down to call out only Pizza and Italian restaurants.
		
	2) Pizza Essentials - A small dataset I created in google maps for us to use. It inclides 22 places in  New York City that are worthy of Pizza pilgrimage.  https://drive.google.com/open?id=1JSRfjOm0ENoiQL1vbxv38UbF_4g_f5CO&usp=sharing

		Google Maps does not give you coordinates but only url links. So I had to create the Latitude/Longitude coordinates from the exported Google Maps list. Please refer to the "Google_Maps_API.ipynb" tutorial notebook for how to get coordinates from Google Maps.

	3) Subway Station Data locations. We'll use the locations
	https://data.cityofnewyork.us/Transportation/Subway-Stations/arq3-7z49

	4) Geopandas New York City Boroughs Polygon, "nybb". Used as a background layer.

## Anlaysis of Python Packages
This group of materials serves as an Analysis of Tools available for mapping and plotting geolocated data.  I attempted to look at most all libraries available to me: Pandas, GeoPandas, Matplotlib, Basemap library, Plotly, MapBox tiles. Folium, Rasterio, Contextily tiles, OpenStreetMap tiles, Shapely, Descartes, SciPy and Google APIs.  

## Assessments
### The Good:
*  Use pandas with Folium for the quickest learning curve and fastest return of a good looking final product.
*  Do not use Google unless you really have to and/or are making some automated process on someone else's dime.
*  SciPy is fantastic for distance math and matrix creation.
*  GeoPandas is only good if you are advanced in geographic modeling because up front knowledge of projections and geodataframe manipulation.
*  Matplotlib is a quick way to plot points but difficult to finish a product in.
*  Plotly is cool stuff and fairly easy to use, but requires API knowledge and a limited amount for free publishing. (Plotting in a notebook is fully free so that's good!)
*  Distances & SciPy:  Euclidean is easiest but Haversine is best because is factors in curve of the earth. Manhattan city block is best for inner-city travel.

### The Bad:
*  Bokeh's API is unreliable.
*  Google Maps API's are just a hard do not use unless you have to.
*  Google Maps regular does not get you Latitude/Longitude coordinates by default and takes quite a bit of work to get them. I believe this is because they want you to integrate fully in their ecosystem.
	#### Note about Google APIs:
	Why is this important?  Up until last year Google API's for mapping were the best go to tool to use, however the API is no longer free and even though we can access them via an API key, some will charge money at all levels of use (im looking at you Google Distance Matrix API)  and in the end, the connection is no reliable nor functions like it used to.


## What's Included:  
Everything needed to run every file and notebook offline. 

You can choose how you want to proceed.  Install all package directly to your computer., or create a virtual environment and install there.
	- Either way, I found that using pip to install directly in the jupyter or Colab notebook was the best way because sometimes Conda and pip do not align.Just add the ! in front of pip to do this in the cell (!pip install folium).

## Order for Notebooks
I would suggest looking at them in this order:

	1)  NYC_Mapping_ETL - Get familiar with the data and how to manipulate it. This is not comprehensive though adn each notebook will have nuances. 
	2) NYC_Mapping_MatPlotLib -  Jump right in to visualizing!   
	3) NYC_Mapping_Plotly - Plotly can be used within the notebooks. No need to send results to their server unless you hasve web access and want to. You will need to create a Plotly account and a MapBox account because they work off each other.  
	4) NYC_Mapping_FOLIUM - Another way to get to see some good stuff. No accounts needed!\
	5) NYC_Mpping_MPL_image  - Mapping over an image has advantages but can be a bit difficult.  Worth checking out.  
	6) NYC_Mapping_GeoDataframes_Geopandas -  This is the optimal way to get the most use of your geosaptial data in Python.  (Note: for best results in finishing the products you will need to use a geodataframe).
	7) NY_Mapping_TSP_Route_Analysis_ETL_1 - How to calculate distances between points using coordinates. How to create distance matrices. How to evaluate distance and choose the best calculations: euclidean, haversine, mahattan, etc.\
	8) NYC_TSP_Route_Analysis_2_Vis - This is a fun one.  It was hard to figure out. But I think it's pretty cool stuff.
	9) NYC_Mapping_Clustering - This is also makes some really cool results.  Lot'ss of great information and cool plots in here.  Even some work with rasters and conversions.
	10) NYC_Mapping_Legend_Scalebar - Adding final touches that will help frame your geospatial product.
	
Others:
	11) NYC_Mapping-Google_OpenStrMap - A walthrough of how to use these tools. But I do not recommend using them. Look for information on how to use their APIs on their document websites.

_______________________________________________

### Setup for Using virtualenv when Using Jupyter

1. Create a virtual environment
```
virtualenv -p Python3 .
```
2. Activate the virtual environment
```
source bin/activate
```
3. Install all dependencies
```
pip install -r requirements.txt
```
4. Start Jupyter
```
jupyter notebook
```
5. Run the jupyter files

### Required API Keys
You will need two keys to make this work:
1. Google API Key: Create an account on https://console.cloud.google.com with a trial of 12 months and get access to the API key for Google Maps JavaScript API.
2. Plotly API Key: Create an account on https://plot.ly/feed/#/ and get an API Key.
