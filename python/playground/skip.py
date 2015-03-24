# break exits the whole execution of function
# continue ignores whatever comes below,
# and 'continues' with next iteration

fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From:'):
		continue
	print line

# opens the file
# strips the whitespace and new lines for every line
# if line does not start with 'From:'
	# continue, which means ignore code below the continue statement
# leaving only lines beginning with 'From:' to be printed
# nicely, without line breaks, taken care of on line 7	