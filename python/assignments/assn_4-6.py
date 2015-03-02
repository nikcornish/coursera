# Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.


# get user input and convert to float
hours = float(raw_input("Please enter your hours: "))
rate = float(raw_input("Please enter your rate: "))


# variables
standardHours = 40
overtimeHours = hours - standardHours
overtimeRate = 1.5
overtimeRate = rate * overtimeRate

# helpful debugging output
# print "You worked " + str(hours) + " standard hours."
# print "You worked " + str(overtimeHours) + " overtime hours."
# print "Your standard rate is " + str(rate) + "."
# print "Your overtime rate is " + str(overtimeRate) + "."

# compute pay function (for both standardHours and overtime calculations)
def computepay(hours,rate):
	
	# gross calculation
	if hours < standardHours:
		gross = hours * rate
		return gross
	
	# overtime calculation
	else:
		gross = (standardHours * rate) + (overtimeHours * overtimeRate)
		return gross


# calling / invoking the function, passing variables assigned from raw_input (lines 9-10),
# and assigning return value to variable "p"
p = computepay(hours,rate)
print p