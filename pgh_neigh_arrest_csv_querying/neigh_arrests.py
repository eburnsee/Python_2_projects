from csv import DictReader

with open('pgh_arrest_data.csv') as arrests:
	# pass file object to the DictReader constructor
	dreader = DictReader(arrests)
	# print(dreader.fieldnames)
	# establish empty dictionary 
	temp_dict = {}
	temp_dict_2 = {}
	neighborhood_list = []
	# iterate through the records to create a list of neighborhoods
	for record in dreader:
		if record['INCIDENTNEIGHBORHOOD'] not in neighborhood_list:
			# fill the list
			neighborhood_list.append(record['INCIDENTNEIGHBORHOOD'])
		# establish dictionary that maps record ID to offenses and neighborhood
		temp_dict[record['PK']] = [record['OFFENSES'], record['INCIDENTNEIGHBORHOOD']]
	# iterate through the neighborhood list we made to make a dictionary that maps neighborhoods to all offenses commited there
	for neighborhood in neighborhood_list:
		list_per_n = []
		for value in temp_dict.values():	
			if neighborhood == value[1]:
				for offense in (value[0].split(" / ")):
					list_per_n.append(offense)
		temp_dict_2[neighborhood]=list_per_n
	# iterate through the keys of our dictionary 
	for neighborhood in sorted(temp_dict_2.keys()):
		print(neighborhood, ':') 
		for offense in sorted(temp_dict_2[neighborhood]):
			print("\t\t", offense)
		print("\n")
	