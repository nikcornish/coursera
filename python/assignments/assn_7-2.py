# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:

# 	X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the lines and compute the average 
# of those values and produce an output as shown below.

# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.



# TODOS

# input file
# find lines with X-DSPAM-Confidence...
# count those lines
# extract the floating point values, and compute average

	# HOW TO FIND AND EXTRACT: search for ":", then grab everything after, or until a line break?
	# HOW TO AVERAGE: add them all together in the loop, then divide by linecount

# print out average in form of "Average spam confidence: 0.750718518519"

filename = raw_input("Please enter a file name: ")
filehandle = open(filename)
linecount = 0
floattotal = 0
for line in filehandle:
	
	if line.startswith("X-DSPAM-Confidence:"):
		linecount = linecount + 1 # total lines with X-DSPAM
		cleanline = line.rstrip() # stripping the \n from the lines
		colonpos = line.find(':')
		myfloat = float(line[colonpos+1:]) # extracts the float and converts to float at same time
		floattotal = floattotal + myfloat

avg = floattotal / linecount
print "Average spam confidence:",avg