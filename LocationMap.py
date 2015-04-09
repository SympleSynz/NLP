import pygmaps
import RegionalDatabase
import string
import sys

if __name__ == "__main__":
	csvData = open("Cat_Data.csv", "r")
	
	#Grab centered lat and long for specific region for creating a map
	RegLat,RegLon = RegionalDatabase.RegionLocation(sys.argv[1])

	#Create the map with zoom option default at 10
	mymap = pygmaps.maps(RegLat, RegLon, 5.3)
	next(csvData)
	for line in csvData:
		if line:
			values = line.split(',')
			b = True
			i = 1
			while(b):
				try:
					float(values[i])
					b = False
				except:
					i += 1
			if values[i] != 0.0 and values[i+1] != 0.0:
				#title = "Person: "+values[4]+"\nOrganization: "+values[5]+"\nFacility: "+values[6]+"\nArtifact: "+values[7]
				#e.g. red "#FF0000", Blue "#0000FF", Green "#00FF00"
				mymap.addpoint(float(values[i]), float(values[i+1]), '#00FF00')

	#Show the map on .html
	mymap.draw('./mymap.html')
	csvData.close()
	
