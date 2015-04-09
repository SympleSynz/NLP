# NLP
Geolocation plotting of Twitter Tweet Data for Crisis Informatics

#Categorized Database with use of Geocode for location identification

Python program that uses annotated data for Named Entity Tagging to create a csv file
with each line being a separate treat, but organized by categories

Also uses Geocoder from google to find latitude, longitude and addresses for locations

##Requirements

Needs separate annotated data by Named Entity Tagging.  Tags must be all caps and 
in the following format: I-LOCATION, B-LOCATIONS, I-FACILITY, etc.

Also needs a region to compare to the results of the geocoder.  
The regions are as listed:
northeast
newengland
midatlantic
eastcoast
gulfcoast
midwest
eastnorthcentral
westnorthcentral
south
southatlantic
eastsouthcentral
westsouthcentral
west
mountain
pacific
westcoast

Each region is broken up by US region and sub regions as well as coastal regions.
Future endeavours will include each state separately.

##Running the Program

The python program must be run in python 2.7 since geocoder doesn't seem to work with 3.4

You will need to install pygeocoder for the library to be imported properly
	
	$sudo pip install pygeocoder

If the pip install does not work and you are running the program from Ubuntu 14.04 VM, it is an issue
with the logs being downloaded improperly into python2.7.  

Once you're able to get pygeocoder installed, the order of command line arguments is:
location, person, organization, facility, artifact, region

  	$python Database.py LOCATION PERSON ORGANIZATION FACILITY ARTIFACT region

On annotated data of 16050 lines long, should take 2m3.017s

##Mapping the Locations

The LocationMap.py imports the program for pygmaps.py.  This will allow pins (can change colors)

to be placed in a mymap.html.  Follow the command line below to map the locations from the csv file.

	$python LocationMap.py region

The region is the same used to parse through the annotated data.  This will grab coordinates to 

center the map.
