def create_icon():
	# loop through to make ten element rows in a list
	for row in row_name_list:
		# loop until we have ten rows of length 10 composed of only 1s and 0s
		while True:
			# gather input
			row_input = input("Please enter ten characters (zeros and ones only, please!) for row " + row + ": ")
			# check if input meets requirements
			if (len(row_input) == 10) and all(((digit == "0") or (digit == "1") for digit in list(row_input))):
				# add input to list
				final_row_list.append(row_input)
				# break out of while loop
				break
			else:
				print("You failed to enter ONLY ten ones and zeros. Please try again.")
				final_row_list.clear()
				continue
	
def display_icon():
	# print the icon
	for row in final_row_list:
		print(row)

def scale_icon():
	# see if the user would like to scale the icon
	scaled_rows = input("Would you like to scale your icon? (yes/no) ")
	if scaled_rows.lower() == "yes":
		scaling_int=int(input("Choose an integer by which to scale? "))
		for row in final_row_list:
			scaled_list = []
			combined_list = []
			row_list=list(row)
			# print(row_list)
			for char in row_list:
				num_row = char[:]*scaling_int
				scaled_list.append(num_row)
			print(*scaled_list, sep="")
			print(*scaled_list, sep="")
			print(*scaled_list, sep="")
			print(*scaled_list, sep="")
			print(*scaled_list, sep="")
	elif scaled_rows.lower() == "no":
		print("Keep it simple, then.")


def invert_icon():
	invert_rows = input("Would you like to invert the icon? (y/n) ")
	if invert_rows.lower() == "yes":
		for row in final_row_list:
			print(row[::-1])
	elif invert_rows.lower() == "no":
		print("Keep it simple, then.")
	else:
		invert_icon()


print("Hello and welcome. You may use this program to display your icon.\nYou will be prompted to enter ten lines of TEN ones and zeros.")
row_name_list = ["one", "two" , "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
final_row_list = []

create_icon()
display_icon()
scale_icon()
invert_icon()
	


