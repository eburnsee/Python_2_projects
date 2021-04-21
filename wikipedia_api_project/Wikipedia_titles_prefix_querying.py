import requests, json

def get_url(search_prefix):
	# base of the url
	API_ENDPOINT = "https://en.wikipedia.org/w/api.php?"
	# parameters appended to url
	actions=("action=query&format=json&list=allpages&apprefix="+ search_prefix +"&aplimit=500")
	# construct full url
	full_url = API_ENDPOINT + actions
	return full_url

#  search wikipedia pages for all pages with a given title prefix
def get_titles(url):
	# uses the url to find the search results and trims results to titles
	# persists perameters across requests
	s=requests.session()
	# makes the request witht he constructed url
	result = s.get(url)
	# convert data to json
	result_2 = json.loads(result.text)
	# store the results as a list
	result_list=[]
	for i in result_2['query']:
		result_list.append(result_2['query'][i])
	# trim data to only titles of pages
	title_list=[]
	for result in result_list[0]:
		title_list.append(dict(result)['title'])
	# return list with the page titles
	return title_list

def get_extract_url(page_title):
	API_ENDPOINT = "https://en.wikipedia.org/w/api.php?"
	# parameters appended to url
	# actions=("action=query&format=json&list=allpages&apprefix="+ search_prefix +"&aplimit=500")
	actions=("action=query&format=json&prop=extracts&explaintext=true&titles=" + page_title)
	full_url = API_ENDPOINT + actions
	return full_url

def get_page_info(full_url):
	# construct full url
	s=requests.session()
	# makes the request witht he constructed url
	result = s.get(full_url)
	# convert data to json
	result_2 = json.loads(result.text)
	# store the results as a list
	result_list=[]
	for i in result_2['query']:
		result_list.append(result_2['query'][i])
	extraction = []
	for result in result_list[1]:
		extraction.append(result_list[1][result]['extract'])
	# info = result_list[1][result]['extract']
	return extraction

def main():	
	print("\n\tThis program can be used to search through the titles of pages on Wikipedia and return a count of the number of page titles\n\t beginning with a given search term. The limit is 500 pages. Thus, the longer and more specific your search term is, the more\n\t accurate your search will be. If your search returns more than 500 results, you will be prompted to enter a more specific search term.")
	while True:
		search_term = input("\n\tFor what title prefix do you want to search?: ")
		result=len(get_titles(get_url(search_term)))
		if result == 500:
			print("\n\tThere are more than", result, "page titles on Wikipedia starting with prefix", (search_term).upper())
			print("\n\tPlease choose a more specific search term.")
			continue 
		elif result == 0:
			print("\n\tThere are", result, "page titles on Wikipedia starting with prefix", (search_term).upper())
			print("\n\tPlease choose a different search term.")
		else:
			print("\n\tThere are", result, "page titles on Wikipedia starting with prefix", (search_term).upper(),"\n")
			titles_opt = input("\tWould you like to see the titles? (yes/no) ")
			print("\n")
			if titles_opt.lower() == "yes":
				for title in get_titles(get_url(search_term)):
					print("\t",title)
				extract_opt = input("\tWould you like to search for the information on one of these pages? (yes/no) ")
				if extract_opt.lower() == "yes":
					try:
						page_title = input("\tFor which page title would you like to search?\n")
						for res in get_page_info(get_extract_url(page_title)):
							print(res)
					except ValueError:
						break
				break
			else:
				break

if __name__=="__main__":
	main()
