emaillist = [] 			
emailtally = dict()		
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
searchString = "From "

for line in fhand :
	if line.startswith(searchString):
		fromlist = line.split()
		emaillist.append(fromlist[1])

for email in emaillist :
	emailtally[email] = emailtally.get(email,0) + 1

biggestEmail = None
biggestCount = None

for email, emailcount in emailtally.items() :
	if biggestCount is None or emailcount > biggestCount :
		biggestEmail = email
		biggestCount = emailcount

print biggestEmail, biggestCount