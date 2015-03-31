# Open the file romeo.txt and read it line by line. 

# For each line, split the line into a list of words using the split() function. 

# For each word on each line check to see if the word is already in the list 
# and if not append it to the list. 

# When the program completes, sort and print the resulting words in alphabetical order. 


#fname = raw_input("Enter file name: ")
textfile = open('romeo.txt')
lst = []

for line in textfile :
	a_line = line.split()

	for word in a_line:
		if word not in lst :
			lst.append(word)

lst.sort()
print lst
	

	










# fname = raw_input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
# print line.rstrip()