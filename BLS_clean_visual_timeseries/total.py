input = open("CES-Data.txt", "r")
#out = open("output.txt", "w")
series_ID = []

for line in input:
	line = line.strip().split("\t")
	series_ID.append(list(line[0].strip()))
print(len(series_ID))
