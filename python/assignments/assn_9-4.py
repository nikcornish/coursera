# 9.4 Write a program to read through the mbox-short.txt and figure out 
# who has the sent the greatest number of mail messages. 

# The program looks for 'From ' lines and takes the second word of those 
# lines as the person who sent the mail. 

# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.

# After the dictionary is produced, the program reads through the dictionary 
# using a maximum loop to find the most prolific committer.


emaillist = [] 			# a list!
emailtally = dict()		# a dictionary!


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)

searchString = "From "


for line in fhand :
	
	# this finds lines starting with From
	# splits each target line into an array
	# adds the 2nd value from each array line to emaillist
	if line.startswith(searchString):
		fromlist = line.split()
		emaillist.append(fromlist[1])


	# this runs for every index in list emaillist
	# either add the value to the dictionary, 
	# or, update the value by 1
for email in emaillist :
	emailtally[email] = emailtally.get(email,0) + 1



# set two variables
biggestEmail = None
biggestCount = None


# ROCKING TWO ITERATION VARIABLES WITH THE FOR LOOP
# for each email, and count in the items of the dictionary
for email, emailcount in emailtally.items() :

	# print each item (eg. both key and value)
	# print email, emailcount

	# if it's None (eg. first round) OR
	# if emailcount is bigger than either first run or previous number
	if biggestCount is None or emailcount > biggestCount :
		# this email is ze biggest AND
		biggestEmail = email
		# this count is the biggest count!
		biggestCount = emailcount

print biggestEmail, biggestCount












# # WORKING WITH DICTIONARY DATA

# # using a for loop on the dictionary
# for derp in emailtally :
# 	print derp, emailtally[derp]

# # prints out the values
# print emailtally.values()