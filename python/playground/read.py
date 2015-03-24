fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if line.startswith('From:'):
		print line

# print statements ADDS a newline
# but there's already a newline in the text file
# = the annoying space!