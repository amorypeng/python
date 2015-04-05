f = open('p18.txt', 'r')
tree = []
s = f.readline()
while(s):
	temp = s.split()
	temp2 = []
	for i in temp:
		temp2.append(int(i))
	tree.append(temp2)
	s = f.readline()
tree.reverse()
f.close()
print(tree)

for i in range(1,len(tree)):
	temp = []
	for j in range(0, len(tree[i])):
		temp.append(tree[i][j] + max(tree[i-1][j], tree[i-1][j+1]))
	tree[i] = temp
print(tree)

