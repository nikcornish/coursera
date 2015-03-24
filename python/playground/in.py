fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not '@uct.ac.za' in line:
		continue
	print line

# open the file
# for each line, strip line space / break characters
# if '@uct.ac.za' is not in line, continue iteration
# otherwise, print line