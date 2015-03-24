# working with secondary memory, where files live?
# when save files, they're saved to SD (2ndary memory)

# open(filename, mode)
# open('mbox.txt', 'r')
# returns a handle to manipulate the file
# filename is a string
# mode is optional, r is read, w is write

# fhand = open('mbox.txt')
# print fhand
# >>> <open file 'mbox.txt',mode 'r' at 0x1005088b0>

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
	count = count + 1

print 'Line Count:', count