import csv
import sys
import RegionalDatabase
#import pygmaps
from pygeocoder import Geocoder
#from itertools import islice, izip, count

if __name__ == "__main__":
	if len(sys.argv) < 7:
		print "Incorrect number of command line arguments"
		print "python2.7 Database.py <Location Data> <Person Data> <Organization Data> <Facility Data> <Artifact Data> <Region>"
		quit()
	LocData = open(sys.argv[1],"r")
	PerData = open(sys.argv[2],"r")
	OrgData = open(sys.argv[3],"r")
	FacData = open(sys.argv[4],"r")
	ArtData = open(sys.argv[5],"r")
	Loc_Data = open("Location_Data.txt", "w")
	Per_Data = open("Person_Data.txt", "w")
	Org_Data = open("Organization_Data.txt", "w")
	Fac_Data = open("Facility_Data.txt", "w")
	Art_Data = open("Artifact_Data.txt", "w")

	#Getting all the location data on single lines to use for geocoding
	for line in LocData:
		strLen = len(line)
		if strLen == 1:
			Loc_Data.write("\n")
			pass
		else:
			line2 = line.rstrip('\n')
			splitLine = line2.split('-')
			splitLen = len(splitLine)
			if splitLine[splitLen-1] == "LOCATION":
				location = splitLine[0]
				if "http" in location:
					Loc_Data.write("")
				else:
					Loc_Data.write("%s " %(location[0:-2]))

	#Getting all Person annotation on single lines to create a linked csv file with each
	for line in PerData:
		strLen = len(line)
		if strLen == 1:
			Per_Data.write("\n")
			pass
		else:
			line2 = line.rstrip('\n')
			splitLine = line2.split('-')
			splitLen = len(splitLine)
			if splitLine[splitLen-1] == "PERSON":
				person = splitLine[0]
				Per_Data.write("%s " %(person[0:-2]))

	#Getting all Organization annotation on a single line to create a csv file
	for line in OrgData:
		strLen = len(line)
		if strLen == 1:
			Org_Data.write("\n")
			pass
		else:
			line2 = line.rstrip('\n')
			splitLine = line2.split('-')
			splitLen = len(splitLine)
			if splitLine[splitLen-1] == "ORGANIZATION":
				organization = splitLine[0]
				Org_Data.write("%s " %(organization[0:-2]))

	#Getting the Facility annotation on a single line to create a csv file
	for line in FacData:
		strLen = len(line)
		if strLen == 1:
			Fac_Data.write("\n")
			pass
		else:
			line2 = line.rstrip('\n')
			splitLine = line2.split('-')
			splitLen = len(splitLine)
			if splitLine[splitLen-1] == "FACILITY":
				facility = splitLine[0]
				Fac_Data.write("%s " %(facility[0:-2]))

	#Getting all the Artifact annotation on a single line to create a csv file
	for line in ArtData:
		strLen = len(line)
		if strLen == 1:
			Art_Data.write("\n")
			pass
		else:
			line2 = line.rstrip('\n')
			splitLine = line2.split('-')
			splitLen = len(splitLine)
			if splitLine[splitLen-1] == "ARTIFACT":
				artifact = splitLine[0]
				Art_Data.write("%s " %(artifact[0:-2]))

	LocData.close()
	PerData.close()
	OrgData.close()
	FacData.close()
	ArtData.close()
	Loc_Data.close()
	Per_Data.close()
	Org_Data.close()
	Fac_Data.close()
	Art_Data.close()

	Loc_Data = open("Location_Data.txt", "r")
	Per_Data = open("Person_Data.txt", "r")
	Org_Data = open("Organization_Data.txt", "r")
	Fac_Data = open("Facility_Data.txt", "r")
	Art_Data = open("Artifact_Data.txt", "r")

	#Need all the data in a list in order to write to CSV file and have all the information available by tweet
	per = []
	org = []
	fac = []
	art = []
	for line in Per_Data:
		per.append(line.strip())

	for line in Org_Data:
		org.append(line.strip())

	for line in Fac_Data:
		fac.append(line.strip())

	for line in Art_Data:
		art.append(line.strip())
	
	#Going to get the location data
	csvData = open("Cat_Data.csv", "w")
	writer = csv.writer(csvData)
	title = ("Location" , "Latitude" , "Longitude" , "GeoCode Address" , "Person" , "Organization" , "Facility" , "Artifact")
	writer.writerow(title)

	#Need to keep track of where I am in the list
	count = 0

	#Created a regional database in a different py file.  Will use the returned region based on what was passed into command line
	reg = RegionalDatabase.region(sys.argv[6])

	for line in Loc_Data:
		strLen = len(line)
		if strLen != 1:
			maps = False	
			try:
				results = Geocoder.geocode(line)
				for i in results:
					j = str(i)
					if j in reg:
							(lat, lng) = i.coordinates
							row = (line.strip() , lat, lng , i, per[count], org[count] , fac[count] , art[count])
							writer.writerow(row)
							maps = True
					else:
						for word in j.split(' '):
							if word in reg:
								(lat, lng) = i.coordinates
								row = (line.strip() , lat , lng ,  i ,  per[count] ,  org[count] ,  fac[count] ,  art[count])
								writer.writerow(row)
								maps = True
				if maps == False:
					(lat, lng) = (0.0, 0.0)
					row = (line.strip() ,  lat ,  lng ,  i ,  per[count] ,  org[count] ,  fac[count] ,  art[count])
					writer.writerow(row)
			except:
				(lat, lng) = (0.0, 0.0)
				row = (line.strip() ,  lat ,  lng , "" ,  per[count] ,  org[count] ,  fac[count] ,  art[count])
				writer.writerow(row)
		else:
			row = ("" ,0.0 ,0.0 ,"" ,  per[count] , org[count] ,  fac[count] ,  art[count])
			writer.writerow(row)
		count += 1
	
	Loc_Data.close()
	Per_Data.close()
	Org_Data.close()
	Fac_Data.close()
	Art_Data.close()
	csvData.close()