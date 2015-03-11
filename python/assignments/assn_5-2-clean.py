largest = None
smallest = None
while True:
    user_input = raw_input("Enter a number: ")
    
    if user_input == "done" :
        break
    else :
        try :
            num = int(user_input)
        except :
            print "Invalid input"
            continue
        
        if largest is None and smallest is None :
            largest = num
            smallest = num
        elif num > largest :
            largest = num
        elif num < smallest :
            smallest = num

print "Maximum is " + str(largest)
print "Minimum is " + str(smallest)