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

# gross calculation
if hours < standardHours:
	gross = hours * rate
	print gross
else:
	gross = (standardHours * rate) + (overtimeHours * overtimeRate)
	print gross