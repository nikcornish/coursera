# write a simple convertor for pounds to kilograms
import math # This imports math module

lbs = raw_input("Enter weight in pounds: ")

def poundsTokg(lbs):
	kgFloat = float(lbs) * 0.453592
	kgString = str(kgFloat)
	print("That's about " + kgString + "kgs")

try:
	val = int(lbs)
	poundsTokg(val)
	
except ValueError:
	print("Please enter a number!")
	lbs2 = raw_input("Do it again!")
	poundsTokg(lbs2)




# need a way to reloop on user input error that without writing it out again and again!!