import csv
import matplotlib.pyplot as plt

# creates a bar chart for races of fugitives
with open('fbi_fugitives.csv', mode='r', encoding="utf-8") as fugitives:
	dreader = csv.DictReader(fugitives)
	race_list = []
	all_races = []
	count_race = []
	for row in dreader:
		if (row['race'] != '') and (row['race'] != "null"):
			all_races.append(row['race'])
	for race in all_races:
		if race not in race_list:
			race_list.append(race)
	for category in race_list:
		counter = 0
		for race in all_races:
			if race == category:
				counter += 1
		# print(category, ":",counter)
		count_race.append(counter)
	plt.bar(race_list, count_race)
	plt.xticks(rotation='vertical')
	axes=plt.gca()
	axes.set_title("FBI Fugitives by Race", fontsize=14, pad=10.0)
	plt.show()
