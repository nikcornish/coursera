filename = raw_input("Enter file name: ")
if len(filename) < 1 : filename = "mbox-short.txt"
fhand = open(filename)
count = 0
for line in fhand:
	line = line.rstrip()
	words = line.split()
	if words == [] :		continue
	if line == '' :			continue
	if words[0] != 'From' :	continue
	print words[1]
	count = count + 1
print "There were", count, "lines in the file with From as the first word"