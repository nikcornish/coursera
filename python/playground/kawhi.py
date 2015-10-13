kawhi_stats = []

name = raw_input("Enter stats file: ")

if len(name) < 1 :
	name = "stats.txt"

fhand = open(name)

for line in fhand :
	if line.startswith("Kawhi "):
		trimmed = line.strip()
		print trimmed