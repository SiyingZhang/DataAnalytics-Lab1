import csv
import urllib

PopulationAndDensity = "http://boxnumbertwo.com/PittsburghData/Population_and_Density.csv"

fhand = urllib.urlopen(PopulationAndDensity)

pop1940to2010= dict()
try:
	reader = csv.reader(fhand)
	next(reader, None)  # skip the headers

	#read data into the dict pop1940to2010
	for row in reader:
		pop1940to2010['%s' % row[0]] = {'pop1940': row[2], 'pop1950': row[3], 'pop1960': row[4], 'pop1970': row[5], 'pop1980': row[6], 'pop1990': row[7], 'pop2000': row[8], 'pop2010': row[9]} 
		
	keys = pop1940to2010.keys()

	print pop1940to2010['Esplen']['pop1940'].replace(',', '')

	#delete comma ',' inside the data(String)
	#But now it doesn't work :(
	for key in pop1940to2010:
		popString = pop1940to2010[key]['pop1940']
		popString.replace(',','')
		print popString
	
	sumOfPop1940 = 0

	#Calculate the sum of population in 1940
	for key in pop1940to2010:
		sumOfPop1940 = sumOfPop1940 + int(pop1940to2010[key]['pop1940']) 

finally:
	fhand.close()