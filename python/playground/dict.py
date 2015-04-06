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



counts = dict()
names = ['bob','james','bob','bob','kate','james','harry']

for name in names : 
	if name not in counts :
		counts[name] = 1
	else :
		counts[name] = counts[name] + 1

print counts