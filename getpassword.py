inp = open('inp.txt', 'r').read().split("\n")

chars = []
for line in inp:
	for char in line:
		if char not in chars:
			chars.append(char)
anom = True
while anom:
	anom = False
	for line in inp:
		prev = 0
		ind = 1
		while ind < len(line):
			earlier = chars.index(line[prev])
			later = chars.index(line[ind])
			if earlier > later:
				anom = True
				temp = chars[earlier]
				chars[earlier] = chars[later]
				chars[later] = temp
			ind += 1
			prev += 1
print()
print("".join(chars))