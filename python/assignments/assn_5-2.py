# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter the numbers from the book for problem 5.1 and Match the desired output as shown.


largest = None
smallest = None

while True:
    
    # ask user for input
    user_input = raw_input("Enter a number: ")
    
    # if user enters done, exit from loop
    if user_input == "done" :
        break
    
    # if not, attempt to convert user_input into an integer for largest and smallest processing
    else :
        
        # if attempt works, assign value to new variable 'num'
        try :
            num = int(user_input)

        # if attempt fails, print feedback message and start again from the top
        except :
            print "Invalid input"

            # the continue statement will not allow the code to continue executing below (solves 'num' undefined error)
            continue
            
            

        # once you get an integer, process it below


        # first iteration using special value 'None'
        if largest is None and smallest is None :
            largest = num
            smallest = num
        
        # if current number is larger than largest, update the larger variable with new largest number
        elif num > largest :
            largest = num

        # if current number is smaller than smallest, update the smallest variable with new smallest number
        elif num < smallest :
            smallest = num


# output the largest and smallest numbers
print "Maximum is " + str(largest)
print "Minimum is " + str(smallest)



