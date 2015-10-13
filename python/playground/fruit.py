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













\