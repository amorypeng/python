names = []
with open('p22.txt') as openfileobject:
	for line in openfileobject:
		names = line.split(',')
#sort
names.sort()

score = 0
for i in range(len(names)):
	#remove the ""
	names[i] = names[i][1:-1]
	#actual calculations, ord('A'-64) = 1
	position = i + 1
	value = 0
	for j in range(len(names[i])):
		value += ord(names[i][j]) - 64
	score += value * position

print(score)

