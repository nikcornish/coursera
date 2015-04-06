# Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours.

# Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation.

# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.

worked_hours = float(raw_input("Enter hours: "))
standard_rate  = float(raw_input("Enter rate: "))

standard_hours = 40
overtime_hours = 0
bonus_rate = 1.5



def computepay():
	
	# if overtime done
	if( worked_hours > standard_hours ):
	

		# calculate overtime hours worked
		overtime_hours = worked_hours - standard_hours


		# normal calculation, plus overtime hours * (rate * bonus_rate)
		gross = (standard_hours * standard_rate) + (overtime_hours * (standard_rate * bonus_rate))
		return gross


	
	# if no overtime
	else:
		gross = worked_hours * standard_rate
		return gross

print("You earned:"),computepay()