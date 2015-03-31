# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.

# Hint: make sure not to include the lines that start with 'From:'.


filename = raw_input("Enter file name: ")
if len(filename) < 1 : filename = "mbox-short.txt"
fhand = open(filename)
count = 0


for line in fhand:
	line = line.rstrip()
	words = line.split()

	# GUARDIAN PATTERNS
	# if it's an empty list, skip it
	if words == [] :		continue

	# if line is empty, skip it
	if line == '' :			continue

	# if first word isn't From, skip it
	if words[0] != 'From' :	continue

	# print out the second word
	print words[1]
	count = count + 1


print "There were", count, "lines in the file with From as the first word"