f = open('p42.txt', 'r')

string = f.read()
words = string.split(',')
triangle = [int(0.5 * var * (var + 1)) for var in range(1,100)] 

count = 0
for i in range(len(words)):
	words[i] = words[i][1:-1]
	checklist = list(words[i])
	checknum = 0
	for letter in checklist:
		checknum += ord(letter) - 64
	if checknum in triangle:
		count += 1
print(count)
f.close()