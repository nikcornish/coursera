fname = raw_input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
count = 0
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
print 'There were',count,'subject lines in',fname



# prompts for file name input from user
# attempts to opens file with try except
# for each line
	# if line 'startswith' Subject
	# count the line
# at the end, nicely print out the count