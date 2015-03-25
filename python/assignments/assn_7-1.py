# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.

# You can download the sample data at http://www.pythonlearn.com/code/words.txt

# fhandle = raw_input("Please enter a file name: ")
# mytext = open(fhandle)
# for line in mytext:
# 	line.rstrip()
# 	print line.upper()


filename = raw_input("Please enter a file name: ")
filehandle = open(filename)
contents = filehandle.read()
cleancontents = contents.rstrip()
capscontents = cleancontents.upper()
print capscontents
