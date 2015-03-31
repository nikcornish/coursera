# 8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() function. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list 
# and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.



# open the damn file
fname = raw_input("Enter file name: ")
textfile = open(fname)

# make an empty list
lst = []


# for every damn line in the text file ...
for line in textfile :
	
	# make into a list
	a_line = line.split()

	# for every word in a single line
	for word in a_line:

		# if the word is not in the list
		if word not in lst :

			# add the damn word
			lst.append(word)


# roll that shit
lst.sort()

# light that shit
print lst

# smoke it!






# SUMMARY
# ---------------------------------------------------
# open the file, then make an empty list.
# for every line in the text file, make into a list
# for every word in each single line ... 
# check if that word is in the (initially empty) list we made
# if it's not there, add it
# sort the list we made
# print the list we made.






