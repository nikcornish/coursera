fname = raw_input("Enter file name: ")
textfile = open(fname)
lst = []
for line in textfile :
	a_line = line.split()
	for word in a_line:
		if word not in lst :
			lst.append(word)
lst.sort()
print lst