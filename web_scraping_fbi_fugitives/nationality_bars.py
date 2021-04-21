import csv
import matplotlib.pyplot as plt

# creates a bar chart for nationalities of fugitives
with open('fbi_fugitives.csv', mode='r', encoding="utf-8") as fugitives:
	dreader = csv.DictReader(fugitives)
	nationality_list = []
	all_nationalities = []
	count_nat = []
	for row in dreader:
		if row['nationality'] != '':
			all_nationalities.append(row['nationality'])
	for nationality in all_nationalities:
		if nationality not in nationality_list:
			nationality_list.append(nationality)
	for category in nationality_list:
		counter = 0
		for nationality in all_nationalities:
			if nationality == category:
				counter += 1
		# print(category, ":",counter)
		count_nat.append(counter)
	plt.bar(nationality_list, count_nat)
	plt.xticks(rotation='vertical')
	axes=plt.gca()
	axes.set_title("FBI Fugitives by Nationality", fontsize=14, pad=10.0)
	plt.show()
	