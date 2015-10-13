# Collections / Dictionaries

# list is a linear collection, 
# indexed by integers, like pringles!

# Dictionaries is not ordered, like a bag of stuff.

# key is the label
# value is the stuff

# -------------------------------------

# purse = dict()
# purse['money'] = 35
# purse['gum'] = 2
# purse['tissues'] = 3

# print purse

# purse['money'] = purse['money'] + 15
# purse['gum'] = purse['gum'] + 7

# print purse
# print "You have $",purse['money']

# -------------------------------------

# counts = dict()
# names = ['bob','james','bob','ted','ted','patrick','bob','andrew']

# for name in names :
# 	if name not in counts :
# 		counts[name] = 1
# 	else :
# 		counts[name] = counts[name] + 1
# print counts




fruitbowl = dict()
fruits = ['apple','banana','orange','apple','strawberry','banana','apple','orange']

for fruit in fruits :
	# for each fruit in fruits array, 
	# either add it to dictionary and set it to zero, 
	# or (it's already in dictionary), so increment it
	fruitbowl[fruit] = fruitbowl.get(fruit,0) + 1
	# create or update

print fruitbowl
print "There are",fruitbowl.get('carrots',0),"carrots in the fruitbowl."
print "There are",fruitbowl.get('apple'),"apples in the fruitbowl."

# the get method returns a value for a given key. 
# if the key is not available, it returns default value None














# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# fhand = open(name)
# ftext = fhand.read()
# flines = ftext.strip(); # this strips excess white space...
# clean = flines.split(); # this turns it into a list, based upon space character

# print len(clean)
# print type(clean)
# print clean[0:10]

# notes made during assn_9-4.py