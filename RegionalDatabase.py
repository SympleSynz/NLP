def region(reg):
	if reg == "northeast":
		NorthEast = ("Connecticut","connecticut","ct","CT","Ct","Maine","maine","me","ME","Me","Massachusetts","massachusetts","MA","ma","Ma","New Hampshire","new hampshire","New hampshire","new Hampshire","NH","nh","Nh","Rhode Island","rhose island","Rhode island","rhode Island","RI","ri","Ri","Vermont","vermont","VT","vt","Vt","New Jersey","new jersey","New jersey","new Jersey","NJ","nj","Nj","New York","new york","New york","new York","NY","ny","Ny","Pennsylvania","pennsylvania","PA","pa","Pa","Connecticut,","connecticut,","ct,","CT,","Ct,","Maine,","maine,","me,","ME,","Me,","Massachusetts,","massachusetts,","MA,","ma,","Ma,","New Hampshire,","new hampshire,","New hampshire,","new Hampshire,","NH,","nh,","Nh,","Rhode Island,","rhose island,","Rhode island,","rhode Island,","RI,","ri,","Ri,","Vermont,","vermont,","VT,","vt,","Vt,","New Jersey,","new jersey,","New jersey,",",new Jersey,","NJ,","nj,","Nj,","New York,","new york,","New york,","new York,","NY,","ny,","Ny,","Pennsylvania,","pennsylvania,","PA,","pa,","Pa,")
		return NorthEast
	elif reg == "newengland":
		NewEngland = ("Connecticut","connecticut","ct","CT","Ct","Maine","maine","me","ME","Me","Massachusetts","massachusetts","MA","ma","Ma","New Hampshire","new hampshire","New hampshire","new Hampshire","NH","nh","Nh","Rhode Island","rhose island","Rhode island","rhode Island","RI","ri","Ri","Vermont","vermont","VT","vt","Vt","Connecticut,","connecticut,","ct,","CT,","Ct,","Maine,","maine,","me,","ME,","Me,","Massachusetts,","massachusetts,","MA,","ma,","Ma,","New Hampshire,","new hampshire,","New hampshire,","new Hampshire,","NH,","nh,","Nh,","Rhode Island,","rhose island,","Rhode island,","rhode Island,","RI,","ri,","Ri,","Vermont,","vermont,","VT,","vt,","Vt,")
		return NewEngland
	elif reg == "midatlantic":
		MidAtlantic = ("New Jersey","new jersey","New jersey","new Jersey","NJ","nj","Nj","New York","new york","New york","new York","NY","ny","Ny","Pennsylvania","pennsylvania","PA","pa","Pa","New Jersey,","new jersey,","New jersey,","new Jersey,","NJ,","nj,","Nj,","New York,","new york,","New york,","new York,","NY,","ny,","Ny,","Pennsylvania,","pennsylvania,","PA,","pa,","Pa,")
		return MidAtlantic
	elif reg == "eastcoast":
		EastCoast = ("Connecticut","connecticut","ct","CT","Ct","Maine","maine","me","ME","Me","Massachusetts","massachusetts","MA","ma","Ma","New Hampshire","new hampshire","New hampshire","new Hampshire","NH","nh","Nh","Rhode Island","rhose island","Rhode island","rhode Island","RI","ri","Ri","New Jersey","new jersey","New jersey","new Jersey","NJ","nj","Nj","New York","new york","New york","new York","NY","ny","Ny","Delaware","delaware","DE","de","De","Maryland","Maryland","MD","md","Md","Washington D.C.","Washington DC","Washington dc","Washington Dc","Washington d.c.","Washington D.c.","washington D.C.","washington DC","washington dc","washington Dc","washington d.c.","washington D.c.","Virginia","virginia","VA","va","Va","North Carolina","north carolina","North carolina","north Carolina","NC","nc","Nc","South Carolina","south carolina","South carolina","south Carolina","SC","sc","Sc","Georgia","georgia","GA","ga","Ga","Florida","florida","FL","fl","Fl","Connecticut,","connecticut,","ct,","CT,","Ct,","Maine,","maine,","me,","ME,","Me,","Massachusetts,","massachusetts,","MA,","ma,","Ma,","New Hampshire,","new hampshire,","New hampshire,","new Hampshire,","NH,","nh,","Nh,","Rhode Island,","rhose island,","Rhode island,","rhode Island,","RI,","ri,","Ri,","New Jersey,","new jersey,","New jersey,","new Jersey,","NJ,","nj,","Nj,","New York,","new york,","New york,","new York,","NY,","ny,","Ny,","Delaware,","delaware,","DE,","de,","De,","Maryland,","Maryland,","MD,","md,","Md,","Washington D.C.,","Washington DC,","Washington dc,","Washington Dc,","Washington d.c.,","Washington D.c.,","washington D.C.,","washington DC,","washington dc,","washington Dc,","washington d.c.,","washington D.c.,","Virginia,","virginia,","VA,","va,","Va,","North Carolina,","north carolina,","North carolina,","north Carolina,","NC,","nc,","Nc,","South Carolina,","south carolina,","South carolina,","south Carolina,","SC,","sc,","Sc,","Georgia,","georgia,","GA,","ga,","Ga,","Florida,","florida,","FL,","fl,","Fl,")
		return EastCoast
	elif reg == "gulfcoast":
		GulfCoast = ("Florida","florida","FL","fl","Fl","Alabama","alabama","AL","al","Al","Mississippi","mississippi","MS","ms","Ms","Louisiana","louisiana","LA","la","La","Texas","texas","TX","tx","Tx","Florida,","florida,","FL,","fl,","Fl,","Alabama,","alabama,","AL,","al,","Al,","Mississippi,","mississippi,","MS,","ms,","Ms,","Louisiana,","louisiana,","LA,","la,","La,","Texas,","texas,","TX,","tx,","Tx,")
		return GulfCoast
	elif reg == "midwest":
		Midwest = ("Illinois","illinois","IL","il","Il","Indiana","indiana","IN","in","In","Michigan","michigan","MI","mi","Mi","Ohio","ohio","OH","oh","Oh","Wisconsin","wisconsin","WI","wi","Wi","Iowa","iowa", "IA","ia","Ia","Kansas","kansas","KS","ks","Ks","Minnesota","minnesota","MN","mn","Mn","Missouri","missouri","MO","mo","Mo","Nebraska","nebraska","NE","ne","Ne","North Dakota","north dakota","North dakota","north Dakota","ND","nd","Nd","South Dakota","south dakota","South dakota","south Dakota","SD","sd","Sd","Illinois,","illinois,","IL,","il,","Il,","Indiana,","indiana,","IN,","in,","In,","Michigan,","michigan,","MI,","mi,","Mi,","Ohio,","ohio,","OH,","oh,","Oh,","Wisconsin,","wisconsin,","WI,","wi,","Wi,","Iowa,","iowa,", "IA,","ia,","Ia,","Kansas,","kansas,","KS,","ks,","Ks,","Minnesota,","minnesota,","MN,","mn,","Mn,","Missouri,","missouri,","MO,","mo,","Mo,","Nebraska,","nebraska,","NE,","ne,","Ne,","North Dakota,","north dakota,","North dakota,","north Dakota,","ND,","nd,","Nd,","South Dakota,","south dakota,","South dakota,","south Dakota,","SD,","sd,","Sd,")
		return Midwest
	elif reg == "eastnorthcentral":
		EastNorthCentral = ("Illinois","illinois","IL","il","Il","Indiana","indiana","IN","in","In","Michigan","michigan","MI","mi","Mi","Ohio","ohio","OH","oh","Oh","Wisconsin","wisconsin","WI","wi","Wi","Illinois,","illinois,","IL,","il,","Il,","Indiana,","indiana,","IN,","in,","In,","Michigan,","michigan,","MI,","mi,","Mi,","Ohio,","ohio,","OH,","oh,","Oh,","Wisconsin,","wisconsin,","WI,","wi,","Wi,")
		return EastNorthCentral
	elif reg == "westnorthcentral":
		WestNorthCentral = ("Iowa","iowa", "IA","ia","Ia","Kansas","kansas","KS","ks","Ks","Minnesota","minnesota","MN","mn","Mn","Missouri","missouri","MO","mo","Mo","Nebraska","nebraska","NE","ne","Ne","North Dakota","north dakota","North dakota","north Dakota","ND","nd","Nd","South Dakota","south dakota","South dakota","south Dakota","SD","sd","Sd","Iowa,","iowa,", "IA,","ia,","Ia,","Kansas,","kansas,","KS,","ks,","Ks,","Minnesota,","minnesota,","MN,","mn,","Mn,","Missouri,","missouri,","MO,","mo,","Mo,","Nebraska,","nebraska,","NE,","ne,","Ne,","North Dakota,","north dakota,","North dakota,","north Dakota,","ND,","nd,","Nd,","South Dakota,","south dakota,","South dakota,","south Dakota,","SD,","sd,","Sd,")
		return WestNorthCentral
	elif reg == "south":
		South = ("Delaware","delaware","DE","de","De","Maryland","Maryland","MD","md","Md","Washington D.C.","Washington DC","Washington dc","Washington Dc","Washington d.c.","Washington D.c.","washington D.C.","washington DC","washington dc","washington Dc","washington d.c.","washington D.c.","Virginia","virginia","VA","va","Va","North Carolina","north carolina","North carolina","north Carolina","NC","nc","Nc","South Carolina","south carolina","South carolina","south Carolina","SC","sc","Sc","Georgia","georgia","GA","ga","Ga","Florida","florida","FL","fl","Fl","West Virginia","west virginia","West virginia","west Virginia","WV","wv","Wv","Alabama","alabama","AL","al","Al","Mississippi","mississippi","MS","ms","Ms","Kentucky","kentucky","KY","ky","Ky","Tennessee","tennessee","TN","tn","Tn","Louisiana","louisiana","LA","la","La","Arkansas","arkansas","AR","ar","Ar","Oklahoma","oklahoma","OK","ok","Ok","Texas","texas","TX","tx","Tx","Delaware,","delaware,","DE,","de,","De,","Maryland,","Maryland,","MD,","md,","Md,","Washington D.C.,","Washington DC,","Washington dc,","Washington Dc,","Washington d.c.,","Washington D.c.,","washington D.C.,","washington DC,","washington dc,","washington Dc,","washington d.c.,","washington D.c.,","Virginia,","virginia,","VA,","va,","Va,","North Carolina,","north carolina,","North carolina,","north Carolina,","NC,","nc,","Nc,","South Carolina,","south carolina,","South carolina,","south Carolina,","SC,","sc,","Sc,","Georgia,","georgia,","GA,","ga,","Ga,","Florida,","florida,","FL,","fl,","Fl,","West Virginia,","west virginia,","West virginia,","west Virginia,","WV,","wv,","Wv,","Alabama,","alabama,","AL,","al,","Al,","Mississippi,","mississippi,","MS,","ms,","Ms,","Kentucky,","kentucky,","KY,","ky,","Ky,","Tennessee,","tennessee,","TN,","tn,","Tn,","Louisiana,","louisiana,","LA,","la,","La,","Arkansas,","arkansas,","AR,","ar,","Ar,","Oklahoma,","oklahoma,","OK,","ok,","Ok,","Texas,","texas,","TX,","tx,","Tx,")
		return South
	elif reg == "southatlantic":
		SouthAtlantic = ("Delaware","delaware","DE","de","De","Maryland","Maryland","MD","md","Md","Washington D.C.","Washington DC","Washington dc","Washington Dc","Washington d.c.","Washington D.c.","washington D.C.","washington DC","washington dc","washington Dc","washington d.c.","washington D.c.","Virginia","virginia","VA","va","Va","North Carolina","north carolina","North carolina","north Carolina","NC","nc","Nc","South Carolina","south carolina","South carolina","south Carolina","SC","sc","Sc","Georgia","georgia","GA","ga","Ga","Florida","florida","FL","fl","Fl","West Virginia","west virginia","West virginia","west Virginia","WV","wv","Wv","Delaware,","delaware,","DE,","de,","De,","Maryland,","Maryland,","MD,","md,","Md,","Washington D.C.,","Washington DC,","Washington dc,","Washington Dc,","Washington d.c.,","Washington D.c.,","washington D.C.,","washington DC,","washington dc,","washington Dc,","washington d.c.,","washington D.c.,","Virginia,","virginia,","VA,","va,","Va,","North Carolina,","north carolina,","North carolina,","north Carolina,","NC,","nc,","Nc,","South Carolina,","south carolina,","South carolina,","south Carolina,","SC,","sc,","Sc,","Georgia,","georgia,","GA,","ga,","Ga,","Florida,","florida,","FL,","fl,","Fl,","West Virginia,","west virginia,","West virginia,","west Virginia,","WV,","wv,","Wv,")
		return SouthAtlantic
	elif reg == "eastsouthcentral":
		EastSouthCentral = ("Alabama","alabama","AL","al","Al","Mississippi","mississippi","MS","ms","Ms","Kentucky","kentucky","KY","ky","Ky","Tennessee","tennessee","TN","tn","Tn","Alabama,","alabama,","AL,","al,","Al,","Mississippi,","mississippi,","MS,","ms,","Ms,","Kentucky,","kentucky,","KY,","ky,","Ky,","Tennessee,","tennessee,","TN,","tn,","Tn,")
		return EastSouthCentral
	elif reg == "westsouthcentral":
		WestSouthCentral = ("Louisiana","louisiana","LA","la","La","Arkansas","arkansas","AR","ar","Ar","Oklahoma","oklahoma","OK","ok","Ok","Texas","texas","TX","tx","Tx","Louisiana,","louisiana,","LA,","la,","La,","Arkansas,","arkansas,","AR,","ar,","Ar,","Oklahoma,","oklahoma,","OK,","ok,","Ok,","Texas,","texas,","TX,","tx,","Tx,")
		return WestSouthCentral
	elif reg == "west":
		West = ("Arizona","arizona","AZ","az","Az","Colorado","colorado","CO","co","Co","Idaho","idaho","ID","id","Id","Montana","montana","MT","mt","Mt","Nevada","nevada","NV","nv","Nv","New Mexico","new mexico","New mexico","new Mexico","NM","nm","Nm","Utah","utah","UT","ut","Ut","Wyoming","wyoming","WY","wy","Wy","Alaska","alaska","AK","ak","Ak","California","california","CA","ca","Ca","Hawaii","hawaii","HI","hi","Hi","Oregon","oregon","OR","or","Or","Washington","washington","WA","wa","Wa","Alaska,","alaska,","AK,","ak,","Ak,","California,","california,","CA,","ca,","Ca,","Hawaii,","hawaii,","HI,","hi,","Hi,","Oregon,","oregon,","OR,","or,","Or,","Washington,","washington,","WA,","wa,","Wa,","Arizona,","arizona,","AZ,","az,","Az,","Colorado,","colorado,","CO,","co,","Co,","Idaho,","idaho,","ID,","id,","Id,","Montana,","montana,","MT,","mt,","Mt,","Nevada,","nevada,","NV,","nv,","Nv,","New Mexico,","new mexico,","New mexico,","new Mexico,","NM,","nm,","Nm,","Utah,","utah,","UT,","ut,","Ut,","Wyoming,","wyoming,","WY,","wy,","Wy,")
		return West
	elif reg == "mountain":
		Mountain = ("Arizona","arizona","AZ","az","Az","Colorado","colorado","CO","co","Co","Idaho","idaho","ID","id","Id","Montana","montana","MT","mt","Mt","Nevada","nevada","NV","nv","Nv","New Mexico","new mexico","New mexico","new Mexico","NM","nm","Nm","Utah","utah","UT","ut","Ut","Wyoming","wyoming","WY","wy","Wy","Arizona,","arizona,","AZ,","az,","Az,","Colorado,","colorado,","CO,","co,","Co,","Idaho,","idaho,","ID,","id,","Id,","Montana,","montana,","MT,","mt,","Mt,","Nevada,","nevada,","NV,","nv,","Nv,","New Mexico,","new mexico,","New mexico,","new Mexico,","NM,","nm,","Nm,","Utah,","utah,","UT,","ut,","Ut,","Wyoming,","wyoming,","WY,","wy,","Wy,")
		return Mountain
	elif reg == "pacific":
		Pacific = ("Alaska","alaska","AK","ak","Ak","California","california","CA","ca","Ca","Hawaii","hawaii","HI","hi","Hi","Oregon","oregon","OR","or","Or","Washington","washington","WA","wa","Wa","Alaska,","alaska,","AK,","ak,","Ak,","California,","california,","CA,","ca,","Ca,","Hawaii,","hawaii,","HI,","hi,","Hi,","Oregon,","oregon,","OR,","or,","Or,","Washington,","washington,","WA,","wa,","Wa,")
		return Pacific
	elif reg == "westcoast":
		WestCoast = ("California","california","CA","ca","Ca","Oregon","oregon","OR","or","Or","Washington","washington","WA","wa","Wa","California,","california,","CA,","ca,","Ca,","Oregon,","oregon,","OR,","or,","Or,","Washington,","washington,","WA,","wa,","Wa,")
		return WestCoast

def RegionLocation(reg):
	if reg == "northeast":
		lat = 42.538394
		lon = -71.153405
		return lat,lon
	elif reg == "newengland":
		lat = 42.796968
		lon = -71.529613
		return lat,lon
	elif reg == "midatlantic":
		lat = 40.865699
		lon = -74.23142
		return lat,lon
	elif reg == "eastcoast":
		lat = 37.71859
		lon = -76.904297
		return lat,lon
	elif reg == "gulfcoast":
		lat = 30.751278
		lon = -89.472656
		return lat,lon
	elif reg == "midwest":
		lat = 42.747012
		lon = -90.966797
		return lat,lon
	elif reg == "eastnorthcentral":
		lat = 41.705729
		lon = -86.572266
		return lat,lon
	elif reg == "westnorthcentral":
		lat = 43.325178
		lon = -96.416016
		return lat,lon
	elif reg == "south":
		lat = 33.94336
		lon = -86.660156
		return lat,lon
	elif reg == "southatlantic":
		lat = 33.578015
		lon = -79.541016
		return lat,lon
	elif reg == "eastsouthcentral":
		lat = 34.741612
		lon = -86.835937
		return lat,lon
	elif reg == "westsouthcentral":
		lat = 32.990236
		lon = -96.767578
		return lat,lon
	elif reg == "west":
		lat = 41.574361
		lon = -113.466797
		return lat,lon
	elif reg == "mountain":
		lat = 41.310824
		lon = -110.214844
		return lat,lon
	elif reg == "pacific":
		lat = 41.967659
		lon = -122.871094
		return lat,lon
	elif reg == "westcoast":
		lat = 38.959409
		lon = -121.289062
		return lat,lon
	#Could add additional 50 for each state