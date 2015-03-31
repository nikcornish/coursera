# total = 0
# count = 0

# while True :
# 	inp = raw_input("Enter number: ")
# 	if inp == 'done': break
# 	value = float(inp)
# 	total = total + value
# 	count = count + 1

# average = total / count
# print 'Average:',average





numlist = []
while True :
	inp = raw_input("Enter number: ")
	if inp == 'done' : break
	value = float(inp)
	numlist.append(value)

average = sum(numlist) / len(numlist)
print 'Average:',average