import requests, csv, time
from bs4 import BeautifulSoup
from fugitive import Fugitive


def find_fugs(url):
	"""opens a page on the fbi's website, iterates through fugitive reocrds, and
	 instantiates fugitive objects with names, urls"""
	# open the link
	fbi_fugs = s.get(url)
	# make the soup
	soup = BeautifulSoup(fbi_fugs.text, 'html.parser')
	# scrape the soup for fugitive record
	name_soup = soup.find_all(class_="name")
	for res in name_soup:
		res_1 = str(res).split('href="')
		res_2 = res_1[1].split('"')
		url = res_2[0]
		# fullname
		name = extract_data(res_2[1])
		name_split = name.split(" ")
		# split the name up; make conditional approach to lack of middle name
		if len(name_split) == 2:
			f_name = name_split[0]
			l_name = name_split[1]
			m_name = "null"
		elif len(name_split) == 3:
			f_name = name_split[0]
			m_name = name_split[1]
			l_name = name_split[2]
		# instantiate the fugitive object
		this_fugitive = Fugitive(l_name, f_name, m_name, url)
		# add the fugitive to the list of fugitive objects
		fugitive_list.append(this_fugitive)

def get_next_page_links(url):
	"""adds the url for the next page to a list so they can be iterated through"""
	fbi_fugs = s.get(url)
	soup = BeautifulSoup(fbi_fugs.text, 'html.parser')
	link_soup = soup.find_all(class_='load-more')
	link_next_1 = str(link_soup).split('href="')
	link_next_2 = link_next_1[1].split('"')
	next_link = link_next_2[0]
	next_page_link_list.append(next_link)

def find_all_fugs():
	"""iterates through all pages and fugitives to give the complete list of fugitive objects"""
	find_fugs(fbi_fugs_url)
	get_next_page_links(fbi_fugs_url)
	for link in next_page_link_list:
		try:
			find_fugs(link)
			get_next_page_links(link)
		except IndexError:
			break

def extract_data(soup_obj):
	"""extracts HTML data from > <"""
	split_left=str(soup_obj).split(">")
	split_right=split_left[1].split("<")
	return split_right[0]

def get_page_data(fugitive):
	"""scrapes additional data from each fugitive's page"""
	this_fug_page = s.get(fugitive.url)
	fug_soup = BeautifulSoup(this_fug_page.text, 'html.parser')
	# summary
	sum_res = fug_soup.find(class_="summary")
	summary=extract_data(sum_res)
	fugitive.summary = summary
	# aliases
	try:
		ali_res = fug_soup.find(class_="wanted-person-aliases").find('p')
		aliases =extract_data(ali_res)
		fugitive.aliases = aliases
	except AttributeError:
		fugitive.aliases ="null"
	# table of data
	try:
		table_res = fug_soup.find(class_="table table-striped wanted-person-description").find_all("td")
		temp_list=[]
		for ele in table_res:
			new_ele=extract_data(ele)
			temp_list.append(new_ele)
		title = temp_list[::2]
		data = temp_list[1::2]
		info_dict = dict(zip(title, data))
		for title, data in info_dict.items():
			if title == 'Date(s) of Birth Used':
				fugitive.dob = data
			if title == 'Place of Birth':	
				fugitive.pob = data
			if title == 'Hair':
				fugitive.hair = data
			if title == 'Eyes':
				fugitive.eyes = data
			if title == 'Height':
				fugitive.height = data
			if title == 'Weight':
				fugitive.weight = data
			if title == 'Sex':
				fugitive.sex = data
			if title == 'Race':
				fugitive.race = data
			if title == 'Nationality':
				fugitive.nationality = data
			if title == 'Scars and Marks':
				fugitive.scars = data
			if title == 'NCIC':
				fugitive.ncic = data
	except AttributeError:
		fugitive.dob = "null"
		fugitive.pob = "null"
		fugitive.hair = "null"
		fugitive.eyes = "null"
		fugitive.height = "null"
		fugitive.weight = "null"
		fugitive.sex = "null"
		fugitive.race = "null"
		fugitive.scars = "null"
		fugitive.ncic = "null"
	# reward
	try:
		reward_res = fug_soup.find(class_="wanted-person-reward").find("p")
		reward = extract_data(reward_res)
		fugitive.reward = reward
	except AttributeError:
		fugitive.reward ="null"
	# remarks
	try:
		remarks_res = fug_soup.find(class_="wanted-person-remarks").find("p")
		remarks = extract_data(remarks_res)
		fugitive.remarks=remarks
	except AttributeError:
		fugitive.remarks = "null"
	# caution
	try:
		caution_res = fug_soup.find(class_="wanted-person-caution").find("p")
		caution = extract_data(caution_res)
		fugitive.caution = caution
	except AttributeError:
		fugitive.caution = "null"
	fugs_w_page_data.append(fugitive)

def write_fug_csv():
	"""writes a csv with information from each fugitive object"""
	with open('fbi_fugitives.csv', mode='w', encoding="utf-8") as fugitives:
		fields=("ncic", "last_name", "first_name", "middle_name", "url", "date_of_birth", "place_of_birth", "hair_color", "eye_color", "height",
					"weight", "sex", "race", "nationality", "scars_and_marks", "reward", "remarks", "caution")
		wr = csv.DictWriter(fugitives, fieldnames=fields, lineterminator="\n")
		wr.writeheader()
		for fugitive in fugs_w_page_data:
			wr.writerow({"ncic": fugitive.ncic, "last_name": fugitive.l_name, "first_name": fugitive.f_name, "middle_name": fugitive.m_name,
							"url": fugitive.url, "date_of_birth": fugitive.dob, "place_of_birth": fugitive.pob, "hair_color": fugitive.hair,
							"eye_color": fugitive.eyes, "height": fugitive.height, "weight": fugitive.weight, "sex": fugitive.sex,
							"race": fugitive.race, "nationality": fugitive.nationality, "scars_and_marks": fugitive.scars, "reward": fugitive.reward, 
							"remarks": fugitive.remarks, "caution": fugitive.caution})
		fugitives.close()

#####################################################################################################################
start = time.time()

s=requests.session()
fbi_fugs_url = "https://www.fbi.gov/wanted/fugitives"
fugitive_list = []
next_page_link_list=[]
find_all_fugs()
fugs_w_page_data=[]
for fugitive in fugitive_list:
	get_page_data(fugitive)
write_fug_csv()

end = time.time()
print(f'\nRUNTIME: {end-start}\n')