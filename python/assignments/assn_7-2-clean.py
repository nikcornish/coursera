filename = raw_input("Please enter a file name: ")
filehandle = open(filename)
linecount = 0
floattotal = 0
for line in filehandle:
	if line.startswith("X-DSPAM-Confidence:"):
		linecount = linecount + 1
		cleanline = line.rstrip()
		colonpos = line.find(':')
		myfloat = float(line[colonpos+1:])
		floattotal = floattotal + myfloat
avg = floattotal / linecount
print "Average spam confidence:",avg